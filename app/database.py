from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import Settings

settings = Settings()

user = settings.POSTGRES_USER
db = settings.POSTGRES_DB
host = settings.POSTGRES_HOST
password = settings.POSTGRES_PASSWORD

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{db}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
