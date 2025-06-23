from fastapi import HTTPException

from database import get_session
from auth.models import User


def get_users():
    Session = get_session()

    with Session() as session:
        return session.query(User).all()


def delete_user(target_user_id):
    Session = get_session()

    with Session() as session:
        user = session.query(User).filter_by(user_id=target_user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        user.delete()
        session.commit()

    return
