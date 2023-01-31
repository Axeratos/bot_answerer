import asyncio
import pathlib

from aiogram import Bot, Dispatcher, Router
from aiogram import types

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
    url = message.chat.username
    chat_object = await get_chat(url)
    image = types.FSInputFile(MEDIA_DIR1.joinpath(chat_object.greeting_image))
    await message.answer_photo(photo=image, caption=chat_object.greeting_text)


if __name__ == '__main__':
    dp.include_router(router)
    db_path = pathlib.Path(__file__).resolve().parent.joinpath("admin_panel/db.sqlite3")
    print("[INFO] Bot started [INFO]")
    print(Config.db.POSTGRES_HOST)
    asyncio.run(dp.start_polling(bot))
