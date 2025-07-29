from fastapi import APIRouter

router = APIRouter()

@router.get("/ping", tags=["health check"])
async def ping():
    return {"message": "pong"}