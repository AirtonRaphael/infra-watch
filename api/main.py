from fastapi import FastAPI

from database import start_db
from config import load_env
from auth.router import router as auth_router
from admin.router import router as admin_router
from hosts.router import router as hosts_router


async def lifespan(app: FastAPI):
    load_env()
    start_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(hosts_router)
