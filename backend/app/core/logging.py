import logging
import os
from logging.handlers import RotatingFileHandler

from app.core.config import settings


def setup_logging():
    os.makedirs(settings.LOG_PATH, exist_ok=True)

    log_file = os.path.join(settings.LOG_PATH, "app.log")

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=3
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)