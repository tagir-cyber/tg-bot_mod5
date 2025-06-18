import aiohttp

from models import User, Rating

class HttpClient:
    def __init__(self):
        self.session = None
        self.host = "https://flask-mod5.onrender.com"
        self.cache = {}

    async def get_session(self):
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
        return self.session

    async def get_user(self, tg_id: int) -> User | None:
        if tg_id in self.cache:
            return self.cache[tg_id]

        session = await self.get_session()
        async with session.get(f"{self.host}/get_user?tg_id={tg_id}") as response:
            if response.status == 200:
                data = await response.json(content_type=None)
                if data["status"] == 200:
                    user = User(**data["body"]["user"])
                    self.cache[tg_id] = user
                    return user
            else:
                print(await response.text())

            return None

    async def create_user(self, tg_id: int, username: str) -> User | None:
        session = await self.get_session()
        async with session.get(f"{self.host}/create_user?tg_id={tg_id}&username={username}") as response:
            if response.status == 200:
                data = await response.json(content_type=None)
                if data["status"] == 200:
                    user = User(**data["body"]["user"])
                    self.cache[tg_id] = user
                    return user
            else:
                print(await response.text())

            return None

    async def get_rating(self) -> list[Rating] | None:
        session = await self.get_session()
        async with session.get(f"{self.host}/get_rating") as response:
            if response.status == 200:
                data = await response.json(content_type=None)
                if data["status"] == 200:
                    return [Rating(**rating) for rating in data["body"]["rating"]]
            else:
                print(await response.text())

            return None

    async def close_session(self):
        if self.session is not None and not self.session.closed:
            await self.session.close()
