from aiohttp import ClientTimeout

from .botapi.rawbotapi import xbot


class get_response:
    @staticmethod
    # Can be used without initialising
    async def json(link: str, params: dict = None):
        session = xbot.session
        async with session.get(
            link, params=params, timeout=ClientTimeout(total=120)
        ) as resp:
            if resp.status != 200:
                raise ValueError
            # Raises an AssertionError if status != 200
            return await resp.json()

    @staticmethod
    async def text(link: str, params: dict = None):
        session = xbot.session
        async with session.get(
            link, params=params, timeout=ClientTimeout(total=120)
        ) as resp:
            if resp.status != 200:
                raise ValueError
            return await resp.text()

    @staticmethod
    async def read(link: str, params: dict = None):
        session = xbot.session
        async with session.get(
            link, params=params, timeout=ClientTimeout(total=120)
        ) as resp:
            if resp.status != 200:
                raise ValueError
            return await resp.read()

    # Just returns the Header
    @staticmethod
    async def status(link: str):
        session = xbot.session
        async with session.get(link) as resp:
            return resp.status
