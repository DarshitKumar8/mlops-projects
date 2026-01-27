import logging
from pathlib import Path

from .config import get_logs_dir, load_config


def setup_logger(name: str) -> logging.Logger:
    """
    Creates and returns a configured logger.
    """
    config = load_config()
    log_level = config["logging"]["level"]

    logs_dir: Path = get_logs_dir()
    logs_dir.mkdir(exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    if not logger.handlers:
        file_handler = logging.FileHandler(logs_dir / "app.log")
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger