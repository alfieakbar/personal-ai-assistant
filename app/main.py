from fastapi import FastAPI
from app.core.engine import get_ai_response
from pydantic import BaseModel

app = FastAPI()


class ChatRequest(BaseModel):
    message: str
    session_id: str = "default_session"


@app.get("/")
def read_root():
    return {"status": "AI Assistant is running"}


@app.post("/chat")
def chat(request: ChatRequest):
    # Kirim session_id ke engine
    response = get_ai_response(request.message, request.session_id)
    return {"response": response}
