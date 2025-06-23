from fastapi import APIRouter, Depends

from admin import services
from auth.schema import UserResponse
from auth.auth import admin_permission

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)


@router.get("/users", response_model=list[UserResponse])
def list_users(user=Depends(admin_permission)):
    users = services.get_users()

    return users


@router.delete("/delete_user")
def delete_user(user_id: int):
    services.delete_user(user_id)

    return
