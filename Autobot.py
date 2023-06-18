import streamlit as st
import requests
def process_user_message(message):
    # You can implement your chatbot logic here to generate a response
    # Example: Send an API request to a backend server and handle the response
    # Once you have the response, return it as the bot's message\
    send_api_request()
    bot_response = "This is a bot response"
    return bot_response

def send_api_request():
    url = 'https://example.com/api'  # Replace with your API endpoint URL

    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Request was successful
            data = response.json()
            # Handle the response data
            print("Response:", data)
        else:
            # Request failed
            print("Request failed with status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        # An error occurred during the request
        print("Request failed:", e)

# Call the function to send the API request
send_api_request()


def main():
    st.markdown("<h1 style='text-align: center;'>LLMD</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Your personal physician*</h3>", unsafe_allow_html=True)

    # Initialize the chat history
    chat_history = st.session_state.get("chat_history", [])

    # Iterate through the chat history and display the messages
    for message in chat_history:
        if message["sender"] == "user":
            st.text_area("You", value=message["text"], key=message["timestamp"], height=80)
        else:
            st.text_area("Bot", value=message["text"], key=message["timestamp"], height=80)

    # User input area
    user_input = st.text_input("Enter your symptoms")

    if st.button("Send"):
        if user_input.strip() != "":
            # Process user message
            bot_response = process_user_message(user_input)

            # Append user message to chat history
            chat_history.append({"sender": "user", "text": user_input})

            # Append bot response to chat history
            chat_history.append({"sender": "bot", "text": bot_response})

            # Clear user input
            user_input = ""

    # Store the chat history in a hidden Streamlit widget to preserve state
    st.write(chat_history, key="chat_history")

st.markdown(
        """
        <div style="position: fixed; bottom: 10px; right: 10px; font-size: 12px; color: gray;">*Not an actual physician</div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()