from pydantic import BaseModel


class LoginSchema(BaseModel):
    username: str
    email: str
    password: str
