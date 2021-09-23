from app.ext.db import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    password = Column(String(100))
    email = Column(String(100), nullable=True)
