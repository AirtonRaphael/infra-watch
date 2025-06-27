from enum import Enum

from pydantic import BaseModel


class PermissionEnum(Enum):
    usuario = "User"
    admin = "Admin"


class CreateUserSchema(BaseModel):
    username: str
    email: str
    password: str
    permission: PermissionEnum = PermissionEnum.usuario


class UpdateUserSchema(BaseModel):
    user_id: int
    username: str
    email: str
    permission: PermissionEnum = PermissionEnum.usuario

class UserResponse(BaseModel):
    user_id: int
    username: str
    email: str
    permission: str

    class Config:
        orm_mode = True

    @classmethod
    def from_orm(cls, obj):
        return cls(
            user_id=obj.user_id,
            username=obj.username,
            email=obj.email,
            permission=obj.permission_str
        )
