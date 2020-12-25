from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart(deep_link=None))
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')
