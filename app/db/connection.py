import asyncpg
from loguru import logger

from .conf import *


async def connection():
    try:
        connection = await asyncpg.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            host=DB_HOST,
            port=DB_PORT
        )
        return connection
    except Exception as error:
        logger.error(error)


async def close_connection(conn: asyncpg.connect()):
    await conn.close()
