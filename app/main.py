from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from tortoise.contrib.fastapi import register_tortoise
from app.route import router
from fastapi.middleware.cors import CORSMiddleware
import os



app = FastAPI()
app.include_router(router)

# ✅ Allow requests from any frontend (during development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <- In production, set specific domain here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Serve frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def serve_homepage():
    return FileResponse("static/index.html")


register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

