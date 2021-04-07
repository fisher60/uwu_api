from fastapi import FastAPI
from api.utils.uwu import to_uwu, stutter

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome"}


@app.get("/uwu/{string}")
async def translate_to_uwu(string: str) -> dict:
    return {"message": stutter(to_uwu(string))}
