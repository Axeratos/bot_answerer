import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, executor, types

load_dotenv()

bot = Bot(token=os.getenv("TOKEN"), parse_mode="HTML")
dp = Dispatcher(bot=bot)


@dp.chat_join_request_handler()
async def join_request(update: types.ChatJoinRequest):
    await update.approve()
    await bot.send_message(update.chat.id, "New user accepted")
    await bot.send_message(
        update.from_user.id, "You entered the private group via invite link"
    )


@dp.channel_post_handler()
async def message_h(message: types.Message):
    await message.answer("New post")
    print(await message.chat.get_url())


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Hello. I am working")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
