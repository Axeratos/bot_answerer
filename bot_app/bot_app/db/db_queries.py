from sqlalchemy import select

from .models import ChatModel
from .db_core import SessionLocal


async def get_chat(invite_link: str) -> ChatModel:
    async with SessionLocal() as session:
        full_link = f"https://t.me/{invite_link}"
        res = await session.execute(select(ChatModel).where(ChatModel.invite_link == full_link))  # noqa
        return res.scalars().first()
