from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
# from .middleware.logger import mw_logger
from .controllers import health

app = FastAPI()

origins = [settings.web_origin]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TODO: Reimplement for robust logging
# app.middleware("http")(mw_logger)

app.include_router(health.router)

@app.get("/", tags=["root"])
async def root():
    return {"message": "\/   /\     /   O   \      /O\  "}