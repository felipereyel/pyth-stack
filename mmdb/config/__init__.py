import os
from dataclasses import dataclass


@dataclass
class Config:
    port: int
    host: str
    log_level: str


def get_config():
    return Config(
        log_level=os.getenv("LOG_LEVEL", "info"),
        port=int(os.getenv("PORT", "3000")),
        host=os.getenv("HOST", "0.0.0.0"),
    )
