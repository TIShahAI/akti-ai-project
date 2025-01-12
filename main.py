from chatbot import chat
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Chatbot API",
    description="A simple chatbot API",
    version="0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ask")
def handle_question(question:str):
    response = chat(question)
    return JSONResponse(content={"response": response})