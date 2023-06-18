# Hackathon-2023

The goal of LLMD is to utilize GPT-4 and analyze WebMD's database to help diagnose patients through their responses.

# Deployment Instructions

1. Launch a redis service at port 6379
2. Set your openai key as an environment variable
3. create a virtual environment and install all packages using `pip install requirements.txt`
4. launch the streamlit app using `streamlit run st_app.py`
