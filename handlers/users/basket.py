import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from handlers.users.main_menu import show_main_menu
from keyboards.default import basket_menu, item_nav_menu
from keyboards.inline.merch_keyboards import buy_item
from keyboards.inline.select_size import sizes_keyboard, clothes_size
from loader import dp
from states import AddToBasket
from utils.db_api.db_commands import get_user, get_item, update_user_total_price, update_user_basket
from utils.db_api.schemas.items import Item
from utils.db_api.schemas.users import User


# Request count of items
async def request_item_count(message: types.Message):
    await message.answer(text=f'Укажите требуемое количество: ')
    await AddToBasket.Count.set()


# Request count of items
async def request_item_size(message: types.Message):
    await message.answer(text=f'Выберете требуемый размер: ', reply_markup=sizes_keyboard())
    await AddToBasket.Size.set()


# Forming new user basket
async def form_user_basket(basket_name: list[str], basket_count: list[int], total_price: int, state: FSMContext) \
        -> (list, list, int):
    async with state.proxy() as data:
        # Get Item
        item: Item = await get_item(data['item_id'])

        # If it yet in basket => update count
        if data['item_name'] in basket_name:
            item_ind = basket_name.index(data['item_name'])
            basket_count[item_ind] += data['item_count']
        else:  # Else add new
            basket_name.append(data['item_name'])
            basket_count.append(data['item_count'])

        # Update total price
        total_price += item.price * data['item_count']

        return basket_name, basket_count, total_price


# Count total price of item and update user basket
async def add_to_basket(user_id: int, message: types.Message, state: FSMContext):
    # Get user
    user: User = await get_user(user_id)

    # Get current user basket and total price
    basket_name: list[str] = user.basket_name
    basket_count: list[int] = user.basket_count
    total_price: int = user.total_price

    # Forming new user basket
    basket_name, basket_count, total_price = await form_user_basket(basket_name=basket_name,
                                                                    basket_count=basket_count,
                                                                    total_price=total_price,
                                                                    state=state)

    # Commit new basket to database
    await update_user_basket(user_id, basket_name, basket_count)

    # Commit new total price to database
    await update_user_total_price(user_id, total_price)

    # Show item navigation menu with next action
    await message.answer(text='Выберете следующее действие: ', reply_markup=item_nav_menu)

    # Finish state
    await state.finish()


# Show current user basket
@dp.message_handler(text='Корзина')
@dp.message_handler(text='Корзина 🧺')
@dp.message_handler(text='Отмена ❌')
@dp.message_handler(Command('basket'))
async def show_goods_basket(message: types.Message):
    # Get user ID
    user_id: int = message.from_user.id

    # Get User
    user: User = await get_user(user_id)

    # Get current user basket
    basket_name: list = user.basket_name
    basket_count: list = user.basket_count

    # Forming basket text
    text: str = ''
    for i in range(len(basket_name)):
        text += f'{i + 1}) {basket_name[i]} x {basket_count[i]} шт.\n'

    # Check for empty basket
    if text == '':
        await message.answer(text=f'Вы пока ничего не добавили в корзину. '
                                  f'Зайдите в раздел с мерчем, там есть много интересного)')
        await show_main_menu(message)
    else:
        await message.answer(text=f'Корзина товаров: ')
        await message.answer(text=text, reply_markup=basket_menu)
        await message.answer(text=f'Общая стоимость: {user.total_price}')


# ADD TO BASKET
# Get item id and request count of item
@dp.callback_query_handler(buy_item.filter())
async def get_item_id(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    # Get item ID
    item_id: int = int(callback_data.get('item_id'))

    # Take item ID to state
    async with state.proxy() as data:
        data['item_id']: int = item_id

    # Request count of item
    await request_item_count(call.message)


# Get count and name of goods and request item size
@dp.message_handler(state=AddToBasket.Count)
async def get_item_count(message: types.Message, state: FSMContext):
    # Get user ID
    user_id: int = message.from_user.id

    async with state.proxy() as data:
        if message.text.isdigit():
            # Get name and count of item
            data['item_count']: int = int(message.text)
            item: Item = await get_item(data['item_id'])
            data['item_name']: str = item.name
            data['user_id']: int = user_id

            # Request size of item
            await request_item_size(message)
        else:
            await message.answer(text=f'Упс) Похоже это не число. Пожалуйста введите число')
            await request_item_count(message)


# Get item name and size
@dp.callback_query_handler(clothes_size.filter(), state=AddToBasket.Size)
async def get_item_name_size(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    # Get item name and size
    async with state.proxy() as data:
        data['item_size']: str = callback_data.get('size')
        data['item_name'] += f' {data["item_size"]}'

    # Add item to basket
    await add_to_basket(data['user_id'], call.message, state)
