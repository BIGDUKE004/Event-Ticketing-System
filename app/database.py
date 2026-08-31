import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("username")
password = os.getenv("password")
database_name = os.getenv("database_name")

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{"Praise28"}:{quote_plus("12345678")}@localhost/{database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()