import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from data import poll_questions
from handlers.users import show_main_menu, ask_user, init_getting, get_user_data
from keyboards.default import poll_menu_first, poll_menu_main, poll_menu_phone
from loader import dp
from states import ReportBug

from utils import send_email, forming_text
from utils.db_api.db_commands import update_user_data


async def finish_report(message: types.Message, state: FSMContext):
    user_id: int = message.from_user.id

    data: dict = await state.get_data()
    update_db_data: dict = {data_name: data[data_name] for data_name in data['update_db']}
    await update_user_data(user_id=user_id, **update_db_data)
    message_text: str = await forming_text.report_bug(user_id, data['report_text'])

    # Email subject
    email_subject: str = 'Новый вопрос'

    # Send email with user question
    await send_email(message_text=message_text, email_subject=email_subject, email_to='upib.ink@gmail.com')

    # Finish state
    await state.finish()

    # Send information about question status to user
    await message.answer(text=f'Ваш вопрос отправлен РДШ! Скоро вам ответят')

    # Return to main menu
    await show_main_menu(message)


@dp.message_handler(Command('report'))
@dp.message_handler(text='Сообщить об ошибке в боте 📍')
@dp.message_handler(text='Сообщить об ошибке в боте')
async def start_report(message: types.Message):
    await message.answer(text=f'Здесь вы можете задать свой вопрос РДШ')

    # Ask for question text
    await ask_user(message=message, state=ReportBug,
                   text=poll_questions['report_text'],
                   markup=poll_menu_first)


@dp.message_handler(state=ReportBug.ReportText)
async def get_report_text(message: types.Message, state: FSMContext):
    await init_getting(message=message, state=state)
    await get_user_data(message=message, main_state=state, data_name='report_text', update_db=False)
    await ask_user(message=message, state=ReportBug, text=poll_questions['name'], markup=poll_menu_main)


@dp.message_handler(state=ReportBug.UserName)
async def get_user_name(message: types.Message, state: FSMContext):
    await get_user_data(message=message, main_state=state, data_name='name')

    await ask_user(message=message, state=ReportBug, text=poll_questions['phone_number'], markup=poll_menu_phone)


@dp.message_handler(state=ReportBug.UserPhoneNumber, content_types=types.ContentTypes.CONTACT)
@dp.message_handler(state=ReportBug.UserPhoneNumber, content_types=types.ContentTypes.TEXT)
async def get_user_phone_number(message: types.Message, state: FSMContext):
    await get_user_data(message=message, main_state=state, data_name='phone_number')

    # Validation data
    async with state.proxy() as data:
        is_valid: bool = (data['phone_number'].isdigit() or (data['phone_number'][1:].isdigit()
                          and data['phone_number'][0] == '+')) and 10 <= len(data['phone_number']) <= 12

        # Check for correct input data
        if is_valid:
            await ask_user(message=message, state=ReportBug, text=poll_questions['email'], markup=poll_menu_main)
        else:
            await ReportBug.previous()
            await message.answer(text=f'Упс) Похоже это не номер телефона. '
                                      f'Пожалуйста проверьте корректность введеных данных')
            await ask_user(message=message, state=ReportBug, text=poll_questions['phone_number'], markup=poll_menu_phone)


@dp.message_handler(state=ReportBug.UserEmail)
async def get_user_email(message: types.Message, state: FSMContext):
    await get_user_data(message=message, main_state=state, data_name='email')

    # Validation data
    async with state.proxy() as data:
        is_valid: bool = bool(re.search(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', data['email']))
        if is_valid:
            markup = ReplyKeyboardRemove()
            await message.answer(text='...', reply_markup=markup)
            await finish_report(message, state)
        else:
            await ReportBug.previous()
            await message.answer(text=f'Пожалуйста введите корректный адрес электронной почты')
            await ask_user(message=message, state=ReportBug, text=poll_questions['email'], markup=poll_menu_main)
