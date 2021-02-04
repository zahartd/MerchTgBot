import logging
import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from data import poll_questions
from keyboards.default import poll_menu_phone, poll_menu_first, poll_menu_main
from loader import dp
from states import Checkout
from utils import forming_text, send_email, gen_checking_code
from utils.db_api.db_commands import update_user_data
from handlers.users import show_main_menu, ask_user, get_user_data, init_getting


# Start checkout order
@dp.message_handler(text='Оформить заказ')
@dp.message_handler(text='Оформить заказ ✅')
@dp.message_handler(Command('checkout'))
async def start_checkout(message: types.Message):
    # Ask user for his/her name
    await ask_user(message=message, state=Checkout, text=poll_questions['name'], markup=poll_menu_first)


# Get client name, commit it to database and request user phone number
@dp.message_handler(state=Checkout.UserName)
async def get_user_name(message: types.Message, state: FSMContext):
    await init_getting(message=message, state=state)
    await get_user_data(message=message, main_state=state, data_name='name')

    await ask_user(message=message, state=Checkout, text=poll_questions['phone_number'], markup=poll_menu_phone)


# Get user phone number
@dp.message_handler(state=Checkout.UserPhoneNumber, content_types=types.ContentTypes.CONTACT)
@dp.message_handler(state=Checkout.UserPhoneNumber, content_types=types.ContentTypes.TEXT)
async def get_user_phone_number(message: types.Message, state: FSMContext):
    await get_user_data(message=message, main_state=state, data_name='phone_number')

    # Validation data
    async with state.proxy() as data:
        is_valid: bool = (data['phone_number'].isdigit() or (data['phone_number'][1:].isdigit()
                          and data['phone_number'][0] == '+')) and 10 <= len(data['phone_number']) <= 12

        # Check for correct input data
        if is_valid:
            await ask_user(message=message, state=Checkout, text=poll_questions['school'], markup=poll_menu_main)
        else:
            await Checkout.previous()
            await message.answer(text=f'Упс) Похоже это не номер телефона. '
                                      f'Пожалуйста проверьте корректность введеных данных')
            await ask_user(message=message, state=Checkout, text=poll_questions['phone_number'], markup=poll_menu_phone)


# Get user school
@dp.message_handler(state=Checkout.UserSchool)
async def get_user_school(message: types.Message, state: FSMContext):
    await get_user_data(message=message, main_state=state, data_name='school')

    # Ask user for his/her living district
    await ask_user(message=message, state=Checkout, text=poll_questions['district'], markup=poll_menu_main)


# Get client name, commit it to database and request user phone number
@dp.message_handler(state=Checkout.UserDistrict)
async def get_user_district(message: types.Message, state: FSMContext):
    await get_user_data(message=message, main_state=state, data_name='district')

    await ask_user(message=message, state=Checkout, text=poll_questions['email_to_check'], markup=poll_menu_main)


@dp.message_handler(state=Checkout.UserEmail)
async def get_user_email(message: types.Message, state: FSMContext):
    await get_user_data(message=message, main_state=state, data_name='email')

    async with state.proxy() as data:
        is_valid: bool = bool(re.search(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', data['email']))
        if is_valid:
            data['checking_code']: str = gen_checking_code()
            message_text: str = forming_text.checking_email(data['checking_code'])
            await send_email(message_text=message_text, email_subject='Код подтверждения от РДШ',
                             email_to=data['email'])
            await ask_user(message=message, state=Checkout, text=poll_questions['checking_code'], markup=poll_menu_main)
        else:
            await Checkout.previous()
            await message.answer(text=f'Пожалуйста введите корректный адрес электронной почты')
            await ask_user(message=message, state=Checkout, text=poll_questions['email'], markup=poll_menu_main)


@dp.message_handler(state=Checkout.Finish)
async def finish_checkout(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == data['checking_code']:
            await message.answer(text=f'Отлично! Ваша заявка пакуется и готовится отпрвится на обработку')

            # Get user ID
            user_id: int = message.from_user.id

            update_db_data: dict = {data_name: data[data_name] for data_name in data['update_db']}

            await update_user_data(user_id=user_id, **update_db_data)

            # Forming email message
            message_text: str = await forming_text.checkout(user_id)

            # Set email subject
            email_subject: str = 'Новый заказ'

            # Send email
            await send_email(message_text=message_text, email_subject=email_subject, email_to='upib.ink@gmail.com')

            # Clean user basket
            await update_user_data(user_id=user_id, basket_name=[], basket_count=[], total_price=0)

            # Finish state
            await state.finish()

            # Send information about order status to user
            await message.answer(text=f'Ваш заказ принят! Скоро с вами свяжутся')

            # Return to main menu
            await show_main_menu(message)
        else:
            await message.answer(text=f'К сожалению код не совпал! Попробуйте еще раз')
            await Checkout.previous()
            data['checking_code']: str = gen_checking_code()
            message_text: str = forming_text.checking_email(data['checking_code'])
            await send_email(message_text=message_text, email_subject='Код подтверждения от РДШ')
            await ask_user(message=message, state=Checkout, text=poll_questions['checking_code'], markup=poll_menu_main)
