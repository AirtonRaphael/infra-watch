from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import settings

SessionLocal = None

Base = declarative_base()


def start_db() -> None:
    global SessionLocal
    engine = create_engine(settings.DB_URL, connect_args={"check_same_thread": False})

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    with SessionLocal() as session:
        yield session


def get_closed_session():
    return SessionLocal
