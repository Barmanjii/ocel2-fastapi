# Main Python Import
from typing import Generator

# Local Backend Import
from app.db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
