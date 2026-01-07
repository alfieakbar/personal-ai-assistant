import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

# Path database SQLite kita
DB_PATH = "sqlite:///./sql_emory.db"


def get_session_history(session_id: str):
    # Ini akan otomatis membuat tabel chat_history jika belum ada
    return SQLChatMessageHistory(session_id=session_id, connection_string=DB_PATH)


def get_ai_response(user_input: str, session_id: str = "default_user"):
    api_key = os.getenv("GOOGLE_API_KEY")

    model = ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash", google_api_key=api_key
    )

    # Modifikasi Prompt agar bisa menerima riwayat percakapan
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Kamu adalah asisten pribadi yang mengingat detail percakapan."),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ]
    )

    output_parser = StrOutputParser()

    chain = prompt | model | output_parser

    # Bungkus chain dengan history provider
    chain_with_history = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )

    return chain_with_history.invoke(
        {"input": user_input}, config={"configurable": {"session_id": session_id}}
    )


# Untuk testing langsung lewat terminal: python app/core/engine.py
if __name__ == "__main__":
    print(get_ai_response("Halo Gemini, apakah kamu sudah aktif?"))
