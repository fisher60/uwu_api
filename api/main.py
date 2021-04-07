from fastapi import FastAPI
from api.utils.uwu import to_uwu, stutter

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome"}


@app.get("/uwu/{string}")
async def translate_to_uwu(string: str) -> dict:
    """Uwuifies a string."""
    return {"message": to_uwu(string)}


@app.get("/stutter/{string}")
@app.get("/uwu-stutter/{string}")
async def translate_to_uwu(string: str) -> dict:
    """Adds uwu *with* a stutter."""
    return {"message": stutter(to_uwu(string))}
