import requests
from bs4 import BeautifulSoup
import string
import os

headers = {'User-Agent': 'YOUR_USER_AGENT'}

# create directory to save files
if not os.path.exists('WebMD_Scraped_Data'):
    os.makedirs('WebMD_Scraped_Data')

# iterate through all pages a to z
for char in string.ascii_lowercase[5:]:
    url = f'https://www.webmd.com/a-to-z-guides/health-topics?pg={char}'
    print(url)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # find the ul element containing the links
    ul = soup.find('ul', class_='az-index-results-group-list')

    # find all li elements (links) in the ul
    for li in ul.find_all('li'):
        link = li.a.get('href')
        if link == '':
            continue
        # follow the link
        link_page = requests.get(link, headers=headers)
        link_soup = BeautifulSoup(link_page.content, 'html.parser')
        # find the body/text of the webpage
        body = link_soup.find('body')

        # check if the body exists
        if body:
            # get all the text within the body
            
            text = ' '.join(p.get_text(strip=True) for p in body.find_all('p'))

            # output the text to a .txt file named after the URL
            filename = link.split('/')[-1] + '.txt'
            print(filename)
            with open(f'WebMD_Scraped_Data/{filename}', 'w', encoding='utf-8') as f:
                f.write(text)
        else:
            print(f"No body found for {link}")