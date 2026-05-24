from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def readiness_check():
    return {
        "status": "ready",
    }