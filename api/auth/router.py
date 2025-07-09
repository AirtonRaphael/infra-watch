from fastapi import APIRouter, HTTPException, Depends

from config import settings
from database import get_session
from .schema import LoginSchema
from .auth import get_user_by_email
from .utils import create_jwt, verify_password


router = APIRouter(
    prefix="/token",
    tags=['auth'],
)


@router.post("/login")
def login(login: LoginSchema, session=Depends(get_session)):
    db_user = get_user_by_email(session, login.email)
    if not db_user:
        raise HTTPException("User does not exist")

    if not verify_password(login.password, db_user.hash_password):
        raise HTTPException(status_code=403, detail="Wrong password!")

    jwt_token = create_jwt(settings.SECRET_KEY, settings.ACCESS_TOKEN_EXPIRE_MINUTES, db_user.user_id, db_user.permission.permission_type)
    refresh = create_jwt(settings.SECRET_KEY, settings.REFRESH_TOKEN_EXPIRE_MINUTES, db_user.user_id, db_user.permission.permission_type)

    return {
        'access_token': jwt_token,
        'refresh_token': refresh,
        'token_type': 'bearer',
    }
