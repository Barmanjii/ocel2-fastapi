from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    This Class will hold all the global Variables
    """

    PROJECT_NAME: str = "ocel2"
    API_V1_STR: str = "/api/v1"
    DB_URL: str | None = ""


settings = Settings()
