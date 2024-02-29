# SQL-Alchemy Imports
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Local Backend Import
from app.core.config import settings


engine = create_engine(settings.DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
