from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    admin_chat_id: str
    db_url: str

    IS_DEBUG: bool = True
    media_dir: str

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore
