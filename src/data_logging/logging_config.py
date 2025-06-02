import logging
from pathlib import Path
from datetime import datetime

def setup_logging(log_dir: str = "logs", verbose: bool = False):
    log_path = Path(log_dir)
    log_path.mkdir(exist_ok=True)

    log_file = log_path / f"climate_data_{datetime.now().strftime('%Y%m%d')}.log"

    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    level = logging.DEBUG if verbose else logging.INFO

    handlers = [
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]

    handlers[0].setLevel(logging.DEBUG)

    handlers[1].setLevel(logging.INFO)

    logging.basicConfig(
        level=level,
        format=log_format,
        handlers=handlers
    )
