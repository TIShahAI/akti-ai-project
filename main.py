from chatbot import chat
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse,HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pathlib import Path


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

templates = Jinja2Templates(directory="templates")

# Serve the chatbot HTML page
@app.get("/", response_class=HTMLResponse)
async def get_chatbot_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/ask")
def handle_question(question:str):
    response = chat(question)
    return JSONResponse(content={"response": response})