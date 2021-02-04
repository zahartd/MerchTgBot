import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import item_nav_menu, poll_menu_first
from keyboards.inline.merch_keyboards import buy_item
from keyboards.inline.select_size import sizes_keyboard, clothes_size
from loader import dp
from states import AddToBasket
from data import poll_questions
from handlers.users import ask_user, get_user_data, init_getting
from utils import form_user_basket
from utils.db_api.db_commands import get_user, get_item, update_user_data
from utils.db_api.schemas.items import Item
from utils.db_api.schemas.users import User


async def finish_add_to_basket(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user: User = await get_user(user_id=data['user_id'])
        basket_name, basket_count, basket_item_price, total_price =\
            await form_user_basket(state_data=data, basket_name=user.basket_name, basket_count=user.basket_count,
                                   basket_item_price=user.basket_item_price, total_price=user.total_price)

        # Commit new basket to database
        await update_user_data(user_id=data['user_id'], basket_name=basket_name, basket_count=basket_count,
                               basket_item_price=basket_item_price, total_price=total_price)

    await state.finish()

    await message.answer(text=f'Товар успешно добавлен в корзину!')

    await message.answer(text=f'Выберете следующее действие: ', reply_markup=item_nav_menu)


# ADD TO BASKET
# Get item id and request count of item
@dp.callback_query_handler(buy_item.filter())
async def start_add_to_basket(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    # Get item ID

    await init_getting(message=call.message, state=state)

    await get_user_data(message=call, main_state=state, data_name='item_id', data_type=int, callback_data=callback_data,
                        update_db=False)
    async with state.proxy() as data:
        item: Item = await get_item(data['item_id'])
        data['item_name']: str = item.name
        data['item_category']: str = item.category_code

    await ask_user(message=call.message, state=AddToBasket, text=poll_questions['item_count'], markup=poll_menu_first)


# Get count and name of goods and request item size
@dp.message_handler(state=AddToBasket.Count)
async def get_item_count(message: types.Message, state: FSMContext):
    await get_user_data(message=message, main_state=state, data_name='item_count', update_db=False)
    # Get user ID
    user_id: int = message.from_user.id
    data = await state.get_data()
    data['user_id'] = user_id
    await state.update_data(data=data)

    async with state.proxy() as data:
        is_valid: bool = data['item_count'].isdigit() and 1 <= int(data['item_count']) <= 100
        if is_valid:
            if data['item_category'] == '1clothes':
                await ask_user(message=message, state=AddToBasket,
                               text=poll_questions['item_size'],
                               markup=sizes_keyboard())
            else:
                markup = ReplyKeyboardRemove()
                await ask_user(message=message, state=AddToBasket, text='...', markup=markup)
                await AddToBasket.Finish.set()
                await finish_add_to_basket(message, state)
        else:
            await AddToBasket.previous()
            await message.answer(text=f'Введите пожалуйста число в интервале от 1 до 100')
            await ask_user(message=message, state=AddToBasket,
                           text=poll_questions['item_count'],
                           markup=poll_menu_first)


# Get item name and size
@dp.callback_query_handler(clothes_size.filter(), state=AddToBasket.Size)
async def get_item_size(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await get_user_data(message=call, main_state=state, data_name='size', callback_data=callback_data, update_db=False)

    async with state.proxy() as data:
        data['item_name'] += f' {data["size"]}'

    markup = ReplyKeyboardRemove()

    await ask_user(message=call.message, state=AddToBasket, text='...', markup=markup)

    await finish_add_to_basket(call.message, state)
