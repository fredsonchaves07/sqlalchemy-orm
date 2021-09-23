from sqlalchemy import Column, Integer, String

from app.ext.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    password = Column(String(100))
    email = Column(String(100), nullable=True)

    def as_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}
