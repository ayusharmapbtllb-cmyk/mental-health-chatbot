
import os
from typing import List, Optional

import openai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Mental Health Chatbot",
    description="A compassionate mental‑health assistant powered by OpenAI GPT models",
    version="1.0.0",
)

# Allow all CORS origins for development convenience
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request / response
class ChatRequest(BaseModel):
    message: str
    history: Optional[List[str]] = None

class ChatResponse(BaseModel):
    reply: str

# System prompt to steer the model toward empathetic, safe replies
SYSTEM_PROMPT = (
    "You are Buddy.Ai , an empathetic mental‑health assistant. "
    "You listen carefully, respond with kindness, and encourage professional help "
    "if the user is in crisis. Always add a short coping suggestion when appropriate."
)

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    """Receive a user message and return an AI response."""
    # Build conversation messages list
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    if req.history:
        for idx, msg in enumerate(req.history):
            role = "user" if idx % 2 == 0 else "assistant"
            messages.append({"role": role, "content": msg})

    messages.append({"role": "user", "content": req.message})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
    )
    reply_text = response.choices[0].message["content"].strip()
    return {"reply": reply_text}
