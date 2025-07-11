from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Hosts(Base):
    __tablename__ = 'Hosts'

    host_id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(unique=True)
    endpoint: Mapped[str]
