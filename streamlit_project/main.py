import streamlit as st
from collections import deque

# Dummy function to simulate chatbot response
def chatbot_response(input_text):
    # Replace this with actual model logic in your implementation
    response = f"Chatbot says: Hi! You said '{input_text}'"
    return response

# Streamlit UI with chat history
def main():
    st.title('LLaMA 3 Chatbot')

    # Initialize chat history as a deque to store messages
    chat_history = deque(maxlen=20)

    user_input = st.text_input("You: ", "")
    if st.button("Send") and user_input.strip() != "":
        # Add user message to chat history
        chat_history.append((True, user_input))

        # Simulate chatbot response (replace with actual model call)
        bot_response = chatbot_response(user_input)
        chat_history.append((False, bot_response))

    st.text_area("Chat History", value='\n'.join(f"{'You:' if is_user else 'LLaMA 3:'} {message}" for is_user, message in chat_history[::-1]), height=400)

if __name__ == "__main__":
    main()
