from fastapi import APIRouter

# router = APIRouter(prefix="/health", tags=["health check"])
router = APIRouter(prefix="/health", tags=["health check"])

@router.get("/ping")
async def ping():
    return {"message": "pong"}