# SQL-Alchemy Imports
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Local Backend Import
from app.core.config import settings
from app.custom_logger import logger


engine = create_engine(settings.DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
try:
    engine.connect()
    logger.info("Connected to the Database!!!")
except Exception as e:
    logger.error("Couldn't connect to the database, Please check...!!")
    """
    Check the Docker Image of postgres is running or not.
    """
    exit()
