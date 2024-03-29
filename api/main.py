from fastapi import FastAPI
from api.utils.uwu import to_uwu, stutter

app = FastAPI(
    title="UwU",
    description="( ᴜ ω ᴜ )",
)


@app.get("/")
async def root():
    return {"message": "Welcome"}


@app.get("/uwu/{string}")
async def translate_to_uwu(string: str) -> dict:
    """Uwuifies a string."""
    return {"message": to_uwu(string)}


@app.get("/stutter/{string}")
async def translate_to_stutter(string: str) -> dict:
    """Makes a string stutter."""
    return {"message": stutter(string)}


@app.get("/uwu-stutter/{string}")
async def translate_to_uwu_and_stutter(string: str) -> dict:
    """Adds uwu *with* a stutter."""
    return {"message": stutter(to_uwu(string))}
