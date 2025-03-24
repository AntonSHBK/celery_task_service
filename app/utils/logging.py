import sys
from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler


def setup_logging(log_dir: str = "logs", log_level: str = "INFO"):
    Path(log_dir).mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # === Общий логгер ===
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    # Консоль
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    api_logger = logging.getLogger("celery")
    api_logger.setLevel(log_level)
    api_file = RotatingFileHandler(Path(log_dir) / "celery.log", maxBytes=5*1024*1024, backupCount=3, encoding="utf-8")
    api_file.setFormatter(formatter)
    api_logger.addHandler(api_file)
    api_logger.propagate = True 

