import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import ReplyKeyboardRemove

from data import poll_questions
from handlers.users import show_goods_basket, ask_user, get_user_data, show_main_menu
from keyboards.default import edit_basket_menu, position_keyboard
from loader import dp
from states import EditBasketDeletePos, EditBasketEditPos
from utils.db_api.db_commands import get_basket_size, get_user_database_data, update_user_data


# Edit current user basket
@dp.message_handler(text='Редактировать корзину')
@dp.message_handler(text='Редактировать корзину ✏')
@dp.message_handler(Command('edit_basket'))
async def edit_basket(message: types.Message):
    await message.answer(text=f'Вы вошли в режим редакирования', reply_markup=edit_basket_menu)


@dp.message_handler(text='Выйти 🔙')
async def back(message: types.Message):
    await show_goods_basket(message)


@dp.message_handler(text='Очистить корзину 🎇')
async def clear_basket(message: types.Message):
    user_id: int = message.from_user.id

    await update_user_data(user_id, basket_name=[], basket_count=[], basket_item_price=[], total_price=0)
    await message.answer(text=f'Корзина очищена 🎇')
    await show_main_menu(message)


@dp.message_handler(text='Удалить позицию ❌')
async def ask_position(message: types.Message):
    user_id: int = message.from_user.id
    basket_size: int = await get_basket_size(user_id)
    await ask_user(message=message, state=EditBasketDeletePos, text=poll_questions['goods_position'],
                   markup=position_keyboard(pos_cnt=basket_size))


@dp.message_handler(text='Редактировать позицию ✏')
async def ask_position(message: types.Message):
    user_id: int = message.from_user.id
    basket_size: int = await get_basket_size(user_id)
    await ask_user(message=message, state=EditBasketEditPos, text=poll_questions['goods_position'],
                   markup=position_keyboard(pos_cnt=basket_size))


@dp.message_handler(state=EditBasketEditPos.Position)
async def ask_count(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardRemove()
    await get_user_data(message=message, main_state=state, data_name='goods_position', update_db=False)
    await ask_user(message=message, state=EditBasketEditPos, text=poll_questions['item_count'], markup=markup)


@dp.message_handler(state=EditBasketDeletePos.Position)
async def delete_position(message: types.Message, state: FSMContext):
    user_id: int = message.from_user.id
    await get_user_data(message=message, main_state=state, data_name='goods_position', update_db=False)

    async with state.proxy() as data:
        is_valid: bool = data['goods_position'].isdigit()

        if is_valid:
            basket_count: list[int] = await get_user_database_data(user_id=user_id, data_name='basket_count')
            basket_name: list[str] = await get_user_database_data(user_id=user_id, data_name='basket_name')
            basket_item_price: list[int] = await get_user_database_data(user_id=user_id, data_name='basket_item_price')
            total_price: int = await get_user_database_data(user_id=user_id, data_name='total_price')

            new_basket_name: list[str] = []
            new_basket_count: list[int] = []
            new_basket_item_price: list[int] = []

            for i, basket_elm in enumerate(zip(basket_name, basket_count, basket_item_price), start=1):
                basket_name_elm = basket_elm[0]
                basket_count_elm = basket_elm[1]
                basket_item_price_elm = basket_elm[2]
                if i != int(data['goods_position']):
                    new_basket_name.append(basket_name_elm)
                    new_basket_count.append(basket_count_elm)
                    new_basket_item_price.append(basket_item_price_elm)
                else:
                    total_price -= basket_item_price_elm * basket_count_elm

            await update_user_data(user_id, basket_name=new_basket_name, basket_count=new_basket_count,
                                   basket_item_price=new_basket_item_price, total_price=total_price)

            await state.finish()
            if total_price == 0:
                await show_goods_basket(message)
            else:
                await show_goods_basket(message, mode='edit')
        else:
            await EditBasketDeletePos.previous()
            await message.answer(text=f'Упс( Похоже вы ввели не число.')
            await ask_position(message)


@dp.message_handler(state=EditBasketEditPos.Count)
async def edit_position(message: types.Message, state: FSMContext):
    user_id: int = message.from_user.id
    await get_user_data(message=message, main_state=state, data_name='item_count', update_db=False)

    async with state.proxy() as data:
        is_valid: bool = data['item_count'].isdigit() and 1 <= int(data['item_count']) <= 100

        if is_valid:
            item_pos: int = int(data['goods_position']) - 1
            basket_item_price: list[int] = await get_user_database_data(user_id=user_id, data_name='basket_item_price')
            new_total_price: int = await get_user_database_data(user_id=user_id, data_name='total_price')
            new_basket_count: list[int] = await get_user_database_data(user_id=user_id, data_name='basket_count')

            new_total_price -= basket_item_price[item_pos] * new_basket_count[item_pos]
            new_basket_count[item_pos] = int(data['item_count'])
            new_total_price += basket_item_price[item_pos] * new_basket_count[item_pos]

            await update_user_data(user_id, basket_count=new_basket_count, total_price=new_total_price)

            await state.finish()
            await show_goods_basket(message, mode='edit')
        else:
            await EditBasketEditPos.previous()
            await message.answer(text=f'Введите пожалуйста число в интервале от 1 до 100')
            await ask_count(message)
