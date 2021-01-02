from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from handlers.users import show_goods_basket
from loader import dp


# Edit current user basket
@dp.message_handler(text='Редактировать корзину')
@dp.message_handler(text='Редактировать корзину ✏')
@dp.message_handler(Command('edit_basket'))
async def edit_basket(message: types.Message):
    await message.answer(text=f'Эта функция скоро заработает')
    await show_goods_basket(message)
