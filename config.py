import os
from dataclasses import dataclass
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()

@dataclass
class Settings:
    api_key: str
    model: str
    env: str
    timeout: int
    max_retries: int

def _get_env(key: str, default=None, required=True):
    value = os.getenv(key, default)
    if required and not value:
        raise RuntimeError(f"Missing required environment variable: {key}")
    return value

@lru_cache()
def get_settings() -> Settings:
    return Settings(
        api_key=_get_env("GOOGLE_API_KEY"),
        model=_get_env("MODEL_NAME", "models/gemini-flash-latest", False),
        env=_get_env("APP_ENV", "production", False),
        timeout=int(_get_env("REQUEST_TIMEOUT", 30, False)),
        max_retries=int(_get_env("MAX_RETRIES", 3, False)),
    )

settings = get_settings()