from functools import wraps
import logging


logger = logging.getLogger(__name__)


def safe_handler(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception:
            logger.exception("Unhandled error in safe_handler")
            raise

    return wrapper
