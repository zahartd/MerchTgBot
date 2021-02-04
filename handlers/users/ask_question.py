import logging
import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from data import poll_questions
from handlers.users import show_main_menu, ask_user
from handlers.users.get_user_data import get_user_data, init_getting
from keyboards.default import poll_menu_first, poll_menu_main, poll_menu_optionally, poll_menu_phone
from loader import dp
from states.ask_question import AskQuestion

from utils import send_email, forming_text
from utils.db_api.db_commands import update_user_data


async def finish_question(message: types.Message, state: FSMContext):
    user_id: int = message.from_user.id

    data: dict = await state.get_data()
    update_db_data: dict = {data_name: data[data_name] for data_name in data['update_db']}
    await update_user_data(user_id=user_id, **update_db_data)
    message_text: str = await forming_text.ask_question(user_id, data['question_text'], data['question_subject'])

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


@dp.message_handler(Command('ask'))
@dp.message_handler(text='Задать вопрос РДШ 📧')
@dp.message_handler(text='Задать вопрос РДШ')
async def start_question(message: types.Message):
    await message.answer(text=f'Здесь вы можете задать свой вопрос РДШ')

    # Ask for question text
    await ask_user(message=message, state=AskQuestion, text=poll_questions['question_text'], markup=poll_menu_first)


@dp.message_handler(state=AskQuestion.QuestionText)
async def get_question_text(message: types.Message, state: FSMContext):
    await init_getting(message=message, state=state)
    await get_user_data(message=message, main_state=state, data_name='question_text', update_db=False)
    await ask_user(message=message, state=AskQuestion, text=poll_questions['question_subject'],
                   markup=poll_menu_optionally)


@dp.message_handler(state=AskQuestion.QuestionSubject)
async def get_question_subject(message: types.Message, state: FSMContext):
    await get_user_data(message=message, main_state=state, data_name='question_subject', update_db=False)

    await ask_user(message=message, state=AskQuestion, text=poll_questions['name'], markup=poll_menu_main)


@dp.message_handler(state=AskQuestion.UserName)
async def get_user_name(message: types.Message, state: FSMContext):
    await get_user_data(message=message, main_state=state, data_name='name')

    await ask_user(message=message, state=AskQuestion, text=poll_questions['phone_number'], markup=poll_menu_phone)


@dp.message_handler(state=AskQuestion.UserPhoneNumber, content_types=types.ContentTypes.CONTACT)
@dp.message_handler(state=AskQuestion.UserPhoneNumber, content_types=types.ContentTypes.TEXT)
async def get_user_phone_number(message: types.Message, state: FSMContext):
    await get_user_data(message=message, main_state=state, data_name='phone_number')

    # Validation data
    async with state.proxy() as data:
        is_valid: bool = (data['phone_number'].isdigit() or (data['phone_number'][1:].isdigit()
                          and data['phone_number'][0] == '+')) and 10 <= len(data['phone_number']) <= 12

        # Check for correct input data
        if is_valid:
            await ask_user(message=message, state=AskQuestion, text=poll_questions['email'], markup=poll_menu_main)
        else:
            await AskQuestion.previous()
            await message.answer(text=f'Упс) Похоже это не номер телефона. '
                                      f'Пожалуйста проверьте корректность введеных данных')
            await ask_user(message=message, state=AskQuestion, text=poll_questions['phone_number'],
                           markup=poll_menu_phone)


@dp.message_handler(state=AskQuestion.UserEmail)
async def get_user_email(message: types.Message, state: FSMContext):
    await get_user_data(message=message, main_state=state, data_name='email')

    # Validation data
    async with state.proxy() as data:
        is_valid: bool = bool(re.search(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', data['email']))
        if is_valid:
            markup = ReplyKeyboardRemove()
            await message.answer(text='...', reply_markup=markup)
            await finish_question(message, state)
        else:
            await AskQuestion.previous()
            await message.answer(text=f'Пожалуйста введите корректный адрес электронной почты')
            await ask_user(message=message, state=AskQuestion, text=poll_questions['email'], markup=poll_menu_main)
