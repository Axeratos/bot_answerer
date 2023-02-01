from aiogram.types import URLInputFile


async def media_url_builder(partial_url) -> URLInputFile:
    return URLInputFile(f"http://proxy:80/media/{partial_url}")
