import logging

logger = logging.getLogger("app")

def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

__all__ = ["configure_logging", "logger"]
