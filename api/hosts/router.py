from fastapi import APIRouter, Depends

from database import get_session
from auth import auth
from .schema import HostSchema, UpdateHostSchema
from .services import get_hosts, insert_host, update_host, delete_host_by_id

router = APIRouter(
    prefix="/hosts",
    tags=["hosts"]
)


@router.get("/list", response_model=list[HostSchema])
def list_host(session=Depends(get_session), token=Depends(auth.JwtBearer())):
    hosts = get_hosts(session)

    return [HostSchema.from_orm(x) for x in hosts]


@router.post("/add")
def add_host(new_host: HostSchema, session=Depends(get_session), token=Depends(auth.admin_permission)):
    host = insert_host(session, new_host)

    return host


@router.post("/update")
def update_host_router(updated_host: UpdateHostSchema, session=Depends(get_session), token=Depends(auth.admin_permission)):
    host = update_host(session, updated_host)

    return host


@router.delete("/delete")
def delete_host(host_id: int, session=Depends(get_session), token=Depends(auth.admin_permission)):
    host = delete_host_by_id(session, host_id)

    return host
