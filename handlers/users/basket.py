import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from handlers.users.main_menu import show_main_menu
from keyboards.default import basket_menu, edit_basket_menu
from loader import dp
from utils.db_api.db_commands import get_user
from utils.db_api.schemas.users import User


# Show current user basket
@dp.message_handler(text='Корзина')
@dp.message_handler(text='Корзина 🧺')
@dp.message_handler(text='Отмена ❌')
@dp.message_handler(Command('basket'))
async def show_goods_basket(message: types.Message, mode: str = 'common'):
    # Get user ID
    user_id: int = message.from_user.id

    # Get User
    user: User = await get_user(user_id)

    # Get current user basket
    basket_name: list[str] = user.basket_name
    basket_count: list[int] = user.basket_count
    basket_item_price: list[int] = user.basket_item_price

    logging.info('Baskeeeeeeeeeeeeeeeeeet')
    logging.info(basket_name)
    logging.info(basket_count)
    logging.info(basket_item_price)

    # Forming basket text
    text: str = ''
    for i in range(len(basket_name)):
        text += f'{i + 1}) {basket_name[i]} ({basket_item_price[i]} руб.) x {basket_count[i]} шт.\n'

    # Check for empty basket
    if text == '':
        await message.answer(text=f'Вы пока ничего не добавили в корзину. '
                                  f'Зайдите в раздел с мерчем, там есть много интересного)')
        await show_main_menu(message)
    else:
        await message.answer(text=f'Корзина товаров: ')
        if mode == 'common':
            await message.answer(text=text, reply_markup=basket_menu)
        else:
            await message.answer(text=text, reply_markup=edit_basket_menu)
        await message.answer(text=f'Общая стоимость: {user.total_price}')
