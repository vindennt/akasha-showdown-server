from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from supabase import create_client, Client, AuthApiError 


import logging

from app.core.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])
logger = logging.getLogger(__name__)

super_client: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

class AuthRequest(BaseModel):
    email: EmailStr
    password: str

def format_auth_response(user, session, message: str):
    if not user or not session:
        raise HTTPException(status_code=401, detail="Authentication failed")

    return {
        "user": {
            "id": user.id,
            "email": user.email,
        },
        "session": {
            "access_token": session.access_token,
            "refresh_token": session.refresh_token,
            "expires_in": session.expires_in,
            "token_type": session.token_type,
        },
        "message": message
    }


@router.post("/signup")
async def auth_signup(payload: AuthRequest):
    try:
        response = super_client.auth.sign_up({
            "email": payload.email,
            "password": payload.password,
        })

        return format_auth_response(response.user, response.session, "Signup & signin successful")

    except AuthApiError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.exception("Unexpected error during signup")
        raise HTTPException(status_code=500, detail="Unexpected error: " + str(e))



@router.post("/signin")
async def auth_signin(payload: AuthRequest):
    try:
        response = super_client.auth.sign_in_with_password({
            "email": payload.email,
            "password": payload.password,
        })
        return format_auth_response(response.user, response.session, "Signin successful")

    except AuthApiError as e:
        raise HTTPException(status_code=401, detail="Authentication failed: " + str(e))
    except Exception as e:
        logger.exception("Unexpected error during signin")
        raise HTTPException(status_code=500, detail="Unexpected error: " + str(e))