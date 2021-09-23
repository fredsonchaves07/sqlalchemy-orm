from app.controllers import create_user
from app.ext.db import Base, engine

Base.metadata.create_all(engine)

user = {"name": "João", "email": "joao@email.com", "password": 123456}

create_user(user)
