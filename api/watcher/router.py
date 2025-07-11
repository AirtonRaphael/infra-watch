from fastapi import APIRouter, Depends

from auth import auth
from .worker import Worker


router = APIRouter(
    prefix="/watcher",
    tags=["watcher"]
)

worker = Worker()


@router.get("/status")
def status(token=Depends(auth.JwtBearer())):
    status = worker.get_status()

    return status


@router.post("/start")
def start(token=Depends(auth.admin_permission)):
    status = worker.start()

    return status


@router.post("/stop")
def stop(token=Depends(auth.admin_permission)):
    status = worker.stop()

    return status
