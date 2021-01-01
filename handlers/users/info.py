from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


# Show information about organisation
@dp.message_handler(text='Информация')
@dp.message_handler(text='Информация ℹ')
@dp.message_handler(Command('info'))
async def bot_info(message: types.Message):
    await message.answer(text=f'Информация о РДШ: ')
    await message.answer(text=f'Скоро здесь будет что-то интересное :)')
