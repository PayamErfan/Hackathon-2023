import streamlit as st
import requests
from gpt_diagnoses import get_gpt_answer

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
    user_input = st.text_input("Enter your symptoms and family history")

    if st.button("Send"):
        if user_input.strip() != "":
            # Process user message
            bot_response = get_gpt_answer(user_input)

            # Append user message to chat history
            chat_history.append({"sender": "user", "text": user_input})

            # Append bot response to chat history
            chat_history.append({"sender": "bot", "text": bot_response})

            # Clear user input
            user_input = ""

    # Store the chat history in a hidden Streamlit widget to preserve state
    st.write(bot_response)

st.markdown(
        """
        <div style="position: fixed; bottom: 10px; right: 10px; font-size: 12px; color: gray;">*Not an actual physician</div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()