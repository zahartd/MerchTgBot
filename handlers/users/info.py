from aiogram import types

from loader import dp


@dp.message_handler(text="/info")
async def bot_info(message: types.Message):
    await message.answer(f'Информация для вас, {message.from_user.full_name}!')
