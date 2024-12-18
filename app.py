from fastapi import FastAPI
from transformers import pipeline
import os

app = FastAPI()

# Load the language model
chat_pipeline = pipeline("text-generation", model="gpt2")

@app.get("/")
async def root():
    return {"message": "Welcome to GovChat AI"}

@app.post("/chat/")
async def chat_with_govchat(message: str):
    response = chat_pipeline(message, max_length=50, num_return_sequences=1)
    return {"response": response[0]["generated_text"]}
