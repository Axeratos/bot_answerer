import asyncio
import pathlib

from aiogram import Bot, Dispatcher, Router
from aiogram import types

from services import media_url_builder
from db.db_queries import get_chat

from core import Config

bot = Bot(token=Config.bot.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
router = Router()

MEDIA_DIR = pathlib.Path(__file__).resolve().parent.parent.joinpath("admin_app/admin_panel/media")
MEDIA_DIR1 = pathlib.Path(__file__).resolve().parent.parent.joinpath("media")


@router.chat_join_request()
async def channel_join_request_handler(join_request: types.ChatJoinRequest):
    await join_request.approve()


@router.channel_post()
async def test(message: types.Message):
    chat_object = await get_chat(message.chat.username)
    if not chat_object:
        return
    image = await media_url_builder(chat_object.greeting_image)
    await message.answer_photo(image, caption=chat_object.greeting_text)


if __name__ == "__main__":
    dp.include_router(router)
    print("[INFO] Bot started [INFO]")
    asyncio.run(dp.start_polling(bot))
