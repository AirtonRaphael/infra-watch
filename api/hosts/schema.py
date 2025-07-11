from typing import Optional

from pydantic import BaseModel


class HostSchema(BaseModel):
    host_id: int
    label: str
    endpoint: str

    class Config:
        from_attributes = True


class UpdateHostSchema(BaseModel):
    host_id: int
    label: Optional[str]
    endpoint: Optional[str]

    class Config:
        from_attributes = True
