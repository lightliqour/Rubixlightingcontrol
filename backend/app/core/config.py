from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    project_name: str
    version: str
    host: str
    port: int
    log_level: str


def load_settings() -> Settings:
    return Settings(
        project_name=os.getenv(
            "RUBIX_PROJECT_NAME",
            "RubixLightingControl",
        ),
        version=os.getenv(
            "RUBIX_VERSION",
            "0.1.0-dev",
        ),
        host=os.getenv(
            "RUBIX_HOST",
            "0.0.0.0",
        ),
        port=int(
            os.getenv(
                "RUBIX_PORT",
                "8000",
            )
        ),
        log_level=os.getenv(
            "RUBIX_LOG_LEVEL",
            "INFO",
        ),
    )


settings = load_settings()