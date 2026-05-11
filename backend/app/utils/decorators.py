"""Custom Decorators"""

import time
import logging
from functools import wraps

logger = logging.getLogger(__name__)


def log_execution_time(func):
    """
    Decorator to log function execution time
    """
    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        execution_time = time.time() - start_time
        logger.info(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result
    
    @wraps(func)
    def sync_wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        logger.info(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result
    
    return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper


import asyncio
