from app.ext.db import session
from app.models import User


def create_user(new_user):
    user = User()

    user.name = new_user.get("name")
    user.password = new_user.get("password")
    user.email = new_user.get("email")

    session.add(user)
    session.commit()


def get_user():
    pass


def list_user():
    pass


def delete_user():
    pass
