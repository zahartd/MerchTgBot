from aiogram import types
from loader import dp


# Echo
@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(text=f'Я не знаю, что это :(')
