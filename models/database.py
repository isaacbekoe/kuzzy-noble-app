import databases
from typing import Callable
from functools import wraps
from config import AppConfig


# create the database handle
db_conn_handle = databases.Database(
    url=AppConfig.DATABASE_URL.value,
    min_size=5,
    max_size=20
)


def db_connection_handler(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper_func(*args, **kwargs) -> None:
        await db_conn_handle.connect()
        data = await func(*args, **kwargs)
        await db_conn_handle.disconnect()
        return data
    return wrapper_func