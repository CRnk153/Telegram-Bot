import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from instruments.weather_parser import Parser
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привіт, {hbold(message.from_user.full_name)}!")
    await message.answer(f"Глянуть погоду: /weather")
    await message.delete()

@dp.message()
async def weather_today(message: Command("weather")) -> None:
    await message.answer(f'{Parser().run()}')
    await message.delete()


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
