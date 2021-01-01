from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from keyboards.default import main_menu
from loader import dp


# Show main menu
@dp.message_handler(text='Главное меню 🕹')
@dp.message_handler(text='Главное меню')
@dp.message_handler(Command('menu'))
async def show_main_menu(message: types.Message):
    await message.answer(text=f'Используйте МЕНЮ, чтобы перейти в нужный раздел', reply_markup=main_menu)
