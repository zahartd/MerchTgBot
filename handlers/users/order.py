from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(text="/order")
async def bot_start(message: types.Message):
    await message.answer(f'Заказ, {message.from_user.full_name}!')
