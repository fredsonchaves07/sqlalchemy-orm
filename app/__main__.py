from app.controllers import create_user, delete_user, get_user, list_user
from app.ext.db import Base, engine

Base.metadata.create_all(engine)

user1 = {"name": "João", "email": "joao@email.com", "password": 123456}
user2 = {"name": "Maria", "email": "maria@email.com", "password": 546321}
user3 = {"name": "Ana", "email": "ana@email.com", "password": 342156}

create_user(user3)

# get_user(1)

# list_user()

# delete_user(2)
