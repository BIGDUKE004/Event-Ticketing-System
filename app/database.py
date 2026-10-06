import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

# Use DATABASE_URL when deployed (Render/Aiven).
# Fall back to the local MySQL settings when running locally.
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
else:
    username = os.getenv("username")
    password = os.getenv("password")
    database_name = os.getenv("database_name")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{username}:{quote_plus(password)}@localhost/{database_name}"
    )

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    connect_args={"ssl": {}}
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
