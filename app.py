import streamlit as st

st.title("Solomon")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.user_role = "user"

# User Role (Questioner or Answerer)
user_role = st.sidebar.checkbox("Switch Role")

if user_role:
    st.session_state.user_role = "assistant"
else:
    st.session_state.user_role = "user"

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    user_message = {"role": st.session_state.user_role, "content": prompt}
    st.session_state.messages.append(user_message)
    # Display user message in chat message container
    with st.chat_message(st.session_state.user_role):
        st.markdown(prompt)

# Add download buttons to the sidebar using st.download_button
if st.sidebar.download_button("Download Conversation as .txt", '\n'.join([f"{message['role']}: {message['content']}" for message in st.session_state.messages]), key="txt"):
    pass  # Clicking the button will trigger the download
