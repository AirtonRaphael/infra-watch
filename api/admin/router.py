from fastapi import APIRouter, Depends

from admin import services
from auth.schema import UserResponse, CreateUserSchema
from auth import auth

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)


@router.get("/users", response_model=list[UserResponse])
def list_users(req_user=Depends(auth.admin_permission)):
    users = services.get_users()

    return users


@router.post("/create_user", response_model=UserResponse)
def create_user(new_user: CreateUserSchema, req_user=Depends(auth.admin_permission)):
    user = auth.create_user(new_user)

    return user


@router.delete("/delete_user")
def delete_user(user_id: int, req_user=Depends(auth.admin_permission)):
    services.delete_user(user_id)

    return
