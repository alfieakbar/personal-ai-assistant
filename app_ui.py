import streamlit as st
import requests

st.set_page_config(page_title="AI Assistant Pro", page_icon="🤖")

st.title("🤖 My Personal AI Assistant")
st.caption("Powered by Gemini 2.5 Flash & FastAPI")

# Input untuk Session ID agar user bisa punya percakapan berbeda
session_id = st.sidebar.text_input("Session ID", value="user_01")
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []

# Inisialisasi history chat di UI
if "messages" not in st.session_state:
    st.session_state.messages = []

# Menampilkan chat lama dari session state streamlit
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input user
if prompt := st.chat_input("Apa yang bisa saya bantu?"):
    # Tampilkan pesan user di UI
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Kirim request ke Backend FastAPI
    with st.chat_message("assistant"):
        with st.spinner("Berpikir..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/chat",
                    json={"message": prompt, "session_id": session_id},
                )
                if response.status_code == 200:
                    ai_response = response.json()["response"]
                    st.markdown(ai_response)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": ai_response}
                    )
                else:
                    st.error("Gagal menghubungi Backend.")
            except Exception as e:
                st.error(f"Error: {str(e)}")
