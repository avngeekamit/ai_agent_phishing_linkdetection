from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agent.cyber_agent import cyber_agent

app = FastAPI(title="AI Cybersecurity Agent")

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (hackathon-safe)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MessageEvent(BaseModel):
    message: str

@app.post("/event/message")
def handle_message_event(data: MessageEvent):
    return cyber_agent(data.message)
