from fastapi import APIRouter, Depends

from auth import auth
from admin import services
from admin.schema import CreateUserSchema, UserResponse, UpdateUserSchema
from database import get_session


router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)


@router.get("/users", response_model=list[UserResponse])
def list_users(req_user = Depends(auth.admin_permission), session = Depends(get_session)):
    users = services.get_users(session)

    return [UserResponse.from_orm(u) for u in users]


@router.post("/create_user", response_model=UserResponse)
def create_user(new_user: CreateUserSchema, req_user = Depends(auth.admin_permission), session = Depends(get_session)):
    user = services.create_user(session, new_user)

    return UserResponse.from_orm(user)


@router.delete("/delete_user")
def delete_user(user_id: int, req_user=Depends(auth.admin_permission), session = Depends(get_session)):
    services.delete_user(session, user_id)

    return


@router.post("/update_user", response_model=UserResponse)
def update_user(updated_user: UpdateUserSchema, req_user = Depends(auth.admin_permission), session = Depends(get_session)):
    user = services.update_user(session, updated_user)

    return user
