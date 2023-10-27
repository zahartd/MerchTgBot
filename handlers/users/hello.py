from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from keyboards.default import main_menu
from loader import dp


# Show main menu
@dp.message_handler(text='Привет')
@dp.message_handler(text='привет')
@dp.message_handler(text='Hello')
@dp.message_handler(text='hello')
@dp.message_handler(text='Здарова')
async def show_main_menu(message: types.Message):
    await message.answer(text=f'Привет 👋) Я бот официального представителя <Название организации скрыто>, я могу показать '
                              f'вам топ активистов, ближайшишие мероприятия и наш мерч, который вы можете '
                              f'выйграть в наших ивентах', reply_markup=main_menu)
