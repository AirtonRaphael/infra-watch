from pydantic import BaseModel
from enum import Enum


class PermissionEnum(Enum):
    usuario = "usuario"
    admin = "admin"


class BaseUserSchema(BaseModel):
    username: str
    email: str
    password: str


class LoginSchema(BaseUserSchema):
    pass


class CreateUserSchema(BaseUserSchema):
    permission: PermissionEnum = PermissionEnum.usuario


class UserResponse(BaseModel):
    user_id: int
    username: str
    email: str

    class Config:
        orm_mode: True
