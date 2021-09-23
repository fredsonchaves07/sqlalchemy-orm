from app.ext.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    settings.get("SQLALCHEMY_DATABASE_URI"),
    echo=settings.get("SQLALCHEMY_TRACK_MODIFICATIONS"),
)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
