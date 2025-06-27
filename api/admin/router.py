from fastapi import APIRouter, Depends, HTTPException

from auth import auth
from admin import services
from admin.schema import CreateUserSchema, UserResponse, UpdateUserSchema


router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)


@router.get("/users", response_model=list[UserResponse])
def list_users(req_user=Depends(auth.admin_permission)):
    users = services.get_users()

    return [UserResponse.from_orm(u) for u in users]


@router.post("/create_user", response_model=UserResponse)
def create_user(new_user: CreateUserSchema, req_user=Depends(auth.admin_permission)):
    user = services.create_user(new_user)

    return user


@router.delete("/delete_user")
def delete_user(user_id: int, req_user=Depends(auth.admin_permission)):
    services.delete_user(user_id)

    return


@router.post("/update_user", response_model=UserResponse)
def update_user(updated_user: UpdateUserSchema, req_user=Depends(auth.admin_permission)):
    user = services.update_user(updated_user)

    return user
