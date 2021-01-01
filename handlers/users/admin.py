from aiogram import types
from loader import dp

from data.config import admins


# Special message for admin
@dp.message_handler(text='secret', user_id=admins)
async def admin_chat_secret(message: types.Message):
    await message.answer(text=f'Это секретное сообщение для админа')
