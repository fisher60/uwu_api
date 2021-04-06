from fastapi import FastAPI
from .utils import uwu

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome"}


@app.get("/uwu/{string}")
async def translate_to_uwu(string: str) -> dict:
    return {"message": uwu.to_uwu(string)}
