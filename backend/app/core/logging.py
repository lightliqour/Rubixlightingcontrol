import logging

from app.config.store import config_store


def configure_logging() -> None:
    config = config_store.load()

    logging.basicConfig(
        level=getattr(
            logging,
            config.log_level.upper(),
            logging.INFO,
        ),
        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        ),
    )