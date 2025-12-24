from fastapi import FastAPI
from pydantic import BaseModel
from backend.intent.embedding_intent import predict_intent_embedding
from backend.orchestrator import handle_intent

app = FastAPI()

class Command(BaseModel):
    text: str

@app.post("/command")
def run_command(cmd: Command):
    intent = predict_intent_embedding(cmd.text)
    result = handle_intent(intent, cmd.text)
    return {"intent": intent, "result": result}