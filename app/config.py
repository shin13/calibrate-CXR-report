from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    CHATGPT_API_ENDPOINT: str
    CHATGPT_MODEL: str = "llama-3.2-3b-instruct"
    ALLOWED_ORIGINS: list = ["http://localhost"]
    HOST: str = "127.0.0.1"
    PORT: int = 7890
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()