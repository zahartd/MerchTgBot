from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from handlers.users import show_main_menu
from keyboards.default import main_menu
from loader import dp


# Edit current user basket
@dp.message_handler(text='Редактировать корзину')
@dp.message_handler(text='Редактировать корзину ✏')
@dp.message_handler(Command('edit_basket'))
async def show_goods_basket(message: types.Message):
    await message.answer(text=f'Эта функция скоро заработает')
    await show_main_menu(message)
