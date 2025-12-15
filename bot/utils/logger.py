from loguru import logger
import sys

logger.remove()


logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>",
)

# Ведение лог файла
"""logger.add(
    "C:/MainProjects/WardenV2/data/debug.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{line} - {message}",
    level="DEBUG",
    rotation="10 MB",     # новый файл каждые 10MB
    compression="zip"     # старый лог архивируется
)"""