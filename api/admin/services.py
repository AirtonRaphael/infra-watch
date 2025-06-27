from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from database import get_session
from auth.models import User, PermissionsType
from auth.utils import get_hashed_password
from .schema import CreateUserSchema, UpdateUserSchema


def get_users():
    Session = get_session()

    with Session() as session:
        return session.query(User).options(joinedload(User.permission)).all()


def create_user(user: CreateUserSchema):
    hash = get_hashed_password(user.password)
    db_user = User(username=user.username, email=user.email, hash_password=hash)

    Session = get_session()
    with Session() as session:
        permission = session.query(PermissionsType).filter_by(permission_type=user.permission.value).first()

        if not permission:
            raise ValueError(f"Permissão '{user.permission}' não encontrada.")

        db_user.permission = permission

        session.add(db_user)
        session.commit()
        session.refresh(db_user)

    return db_user


def delete_user(target_user_id):
    Session = get_session()

    with Session() as session:
        user = session.query(User).filter_by(user_id=target_user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        user.delete()
        session.commit()

    return


def update_user(updated_user: UpdateUserSchema):
    Session = get_session()

    with Session() as session:
        db_user = session.query(User).filter_by(user_id=updated_user.user_id).first()
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")

        permission = session.query(PermissionsType).filter_by(permission_type=updated_user.permission.value).first()
        if not permission:
            raise HTTPException(status_code=400, detail="Invalid permission")


        db_user.username = updated_user.username
        db_user.email = updated_user.email
        db_user.permission = permission

        session.commit()
    
    return updated_user

