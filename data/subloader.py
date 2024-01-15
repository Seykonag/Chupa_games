import os

from ujson import loads
import aiofiles


async def get_json(filename: str) -> dict:
    path = f'data/{filename}.json'

    if os.path.exists(path):
        async with aiofiles.open(path, 'r', encoding='utf-8') as file:
            return loads(await file.read())

    return {}
