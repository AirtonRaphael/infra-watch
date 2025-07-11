from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from utils import is_valid_url
from .models import Hosts
from .schema import HostSchema, UpdateHostSchema


def get_hosts(session: Session):

    return session.query(Hosts).all()


def insert_host(session: Session, new_host: HostSchema):
    endpoint = new_host.endpoint

    if not is_valid_url(endpoint):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid url')

    host = Hosts(
        label=new_host.label,
        endpoint=endpoint
    )

    session.add(host)
    session.commit()
    session.refresh(host)

    return host


def update_host(session: Session, updated_host: UpdateHostSchema):
    host = session.query(Hosts).filter_by(host_id=updated_host.host_id).first()

    if not host:
        raise HTTPException(status_code=status.HTTP_404_NOF_FOUND, detail='User not found')

    label = updated_host.label
    if label:
        host.label = label

    endpoint = updated_host.endpoint
    if endpoint:
        host.endpoint = endpoint

    session.commit()
    session.refresh(host)

    return host


def delete_host_by_id(session: Session, host_id: int):
    host = session.query(Hosts).filter_by(host_id=host_id).first()

    if not host:
        raise HTTPException(status_code=status.HTTP_404_NOF_FOUND, detail='User not found')
    print(host)
    session.delete(host)
    session.commit()

    return host
