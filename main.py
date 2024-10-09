import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import TOKEN

HELP_COMMANDS = """
<b>/help</b> - <em>Показывает список команд</em>
<b>/sticker</b> - <em>Отправляет id стикера в ответ на отправленный стикер</em>
<b>/start</b> - <em>Запускает бота</em>
"""

HELLO = "Добро пожаловать! список команд - /help"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_heandler(message: Message) -> None:
    await message.answer(HELLO)


@dp.message(F.text == "/help")
async def help_heandler(message: Message) -> None:
    await message.answer(HELP_COMMANDS)

@dp.message(F.text == "/sticker")
async def sticker_handler(message: Message) -> None:
    await message.answer("Отправьте стикер")

@dp.message(F.sticker)
async def sticker_id_handler(message: Message) -> None:
    await message.answer(message.sticker.file_id)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())



































