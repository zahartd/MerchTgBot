from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp


# Show list of top school
@dp.message_handler(text='Список активистов')
@dp.message_handler(text='Список активистов 📃')
@dp.message_handler(Command('list'))
async def bot_start(message: types.Message):
    await message.answer(text=f'Список активистов: ')
    await message.answer(text=f'Скоро здесь будет что-то интересное :)')
