from fastapi import HTTPException, status
from sqlalchemy.orm import joinedload, Session

from auth.models import User, PermissionsType
from auth.utils import get_hashed_password
from auth.auth import get_user_by_email
from .schema import CreateUserSchema, UpdateUserSchema


def get_users(session: Session):
    return session.query(User).options(joinedload(User.permission)).all()


def create_user(session: Session, user: CreateUserSchema):
    hash = get_hashed_password(user.password)

    user = get_user_by_email(session, user.email)
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User already exists')

    db_user = User(username=user.username, email=user.email, hash_password=hash)

    permission = session.query(PermissionsType).filter_by(permission_type=user.permission.value).first()
    if not permission:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Permission '{user.permission}' not found")

    db_user.permission = permission

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


def delete_user(session: Session, target_user_id: int):
    user = session.query(User).filter_by(user_id=target_user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    user.delete()
    session.commit()

    return


def update_user(session: Session, updated_user: UpdateUserSchema):
    db_user = session.query(User).filter_by(user_id=updated_user.user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    permission = session.query(PermissionsType).filter_by(permission_type=updated_user.permission.value).first()
    if not permission:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid permission")


    db_user.username = updated_user.username
    db_user.email = updated_user.email
    db_user.permission = permission

    session.commit()
    session.refresh(db_user)
    
    return db_user
