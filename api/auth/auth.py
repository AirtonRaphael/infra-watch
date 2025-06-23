from typing import Optional

from fastapi import Request, HTTPException, Depends, status
from fastapi.security import HTTPBearer
from jwt.exceptions import ExpiredSignatureError, PyJWTError
from sqlalchemy.orm import joinedload

from .models import User, PermissionsType
from .schema import CreateUserSchema
from .utils import get_hashed_password, decode_jwt
from database import get_session


def get_user_by_id(user_id: int):
    Session = get_session()

    with Session() as session:
        return session.query(User).options(joinedload(User.permission)).filter_by(user_id=user_id).first()


def get_user_by_email(email: str):
    Session = get_session()

    with Session() as session:
        return session.query(User).options(joinedload(User.permission)).filter_by(email=email).first()


def create_user(user: CreateUserSchema):
    hash = get_hashed_password(user.password)
    db_user = User(username=user.username, email=user.email, hash_password=hash)

    Session = get_session()
    with Session() as session:

        permission = session.query(PermissionsType).filter_by(name=user.permission).first()

        if not permission:
            raise ValueError(f"Permissão '{user.permission}' não encontrada.")

        db_user.permission = permission

        session.add(db_user)
        session.commit()
        session.refresh(db_user)

    return db_user


class JwtBearer(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super(JwtBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        credential = await super(JwtBearer, self).__call__(request)
        if not credential:
            raise HTTPException(status_code=403, detail="Invalid authorization code")
        
        if not credential.scheme == "Bearer":
            raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
        
        token = credential.credentials

        if not self.validate_jwt(token):
            raise HTTPException(status_code=403, detail="Invalid token")
        
        return token

    def validate_jwt(self, jwt_token: str) -> bool:
        try:
            decode_jwt(jwt_token)
            return True
        except ExpiredSignatureError:
            return False
        except PyJWTError:
            return False


def get_payload(token: str = Depends(JwtBearer())) -> User:
    payload = decode_jwt(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token or expired token"')

    return payload


def admin_permission(payload=Depends(get_payload)):
    if payload.get('role', '') != "Admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid permission')

    return payload
