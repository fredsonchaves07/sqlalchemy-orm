from app.ext.db import session
from app.models import User


def create_user(new_user):
    user = User()

    user.name = new_user.get("name")
    user.password = new_user.get("password")
    user.email = new_user.get("email")

    session.add(user)
    session.commit()


def get_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()

    print(user.as_dict())


def list_user():
    users = session.query(User).all()

    list_users = [user.as_dict() for user in users]

    print(list_users)


def delete_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()

    session.delete(user)
    session.commit()
