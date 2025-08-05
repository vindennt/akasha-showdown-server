from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from supabase import create_client, Client, AuthApiError 


import logging

from app.core.config import settings

router = APIRouter(tags=["auth"])
logger = logging.getLogger(__name__)

super_client: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

class SignUpRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/auth/signup")
async def auth_signup(payload: SignUpRequest):
    try:
        response = super_client.auth.sign_up({
            "email": payload.email,
            "password": payload.password,
        })

        user = response.user
        session = response.session

        return {
            "user": {
                "id": user.id if user else None,
                "email": user.email if user else None,
            },
            "session": {
                "access_token": session.access_token if session else None,
                "refresh_token": session.refresh_token if session else None,
                "expires_in": session.expires_in if session else None,
                "token_type": session.token_type if session else None,
            },
            "message": "Signup successful"
        }

    # Supabase error handling
    except AuthApiError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.exception("Unexpected error during signup")
        raise HTTPException(status_code=500, detail="Unexpected error: " + str(e))
