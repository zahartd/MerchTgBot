import logging
from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from data import poll_questions
from data.config import admins
from handlers.users import show_main_menu, ask_user, init_getting, get_user_data
from keyboards.default import poll_menu_first, poll_menu_main
from loader import dp, bot
from states import Mailing
from utils.db_api.db_commands import get_all_users, get_users_by_project
from utils.db_api.schemas.users import User


@dp.message_handler(Command('tell_everyone'), user_id=admins)
async def start_everyone_mailing(message: types.Message):
    await message.answer('Пришлите текст рассылки: ')
    await Mailing.TextEveryOne.set()


@dp.message_handler(user_id=admins, state=Mailing.TextEveryOne)
async def everyone_mailing(message: types.Message, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    await state.reset_state()

    users = await get_all_users()
    for user in users:
        try:
            await bot.send_message(chat_id=user.user_id, text=text)
            await sleep(0.3)
        except Exception:
            logging.info('Mailing error!!!')

    await message.answer('Рассылка выполнена')


@dp.message_handler(Command('bsj_mail'), user_id=admins)
async def start_projects_mailing(message: types.Message):
    await message.answer('Пришлите текст рассылки: ')
    await Mailing.TextProjects.set()


@dp.message_handler(user_id=admins, state=Mailing.TextProjects)
async def projects_mailing(message: types.Message, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    await state.reset_state()

    users = await get_users_by_project(project='bsj')
    for user in users:
        try:
            await bot.send_message(chat_id=user.user_id, text=text)
            await sleep(0.3)
        except Exception:
            logging.info('Mailing error!!!')

    await message.answer('Рассылка выполнена')


@dp.message_handler(Command('tell_one'), user_id=admins)
async def start_one_mailing(message: types.Message):
    await message.answer('Пришлите текст рассылки: ')
    await Mailing.TextOne.set()


@dp.message_handler(user_id=admins, state=Mailing.TextOne)
async def get_mailing_text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text

    await message.answer('Пришлите ID пользователя, котрому хотите написать: ')
    await Mailing.ID.set()


@dp.message_handler(user_id=admins, state=Mailing.ID)
async def one_mailing(message: types.Message, state: FSMContext):
    user_id: str = message.text
    data = await state.get_data()
    text: str = data.get('text')
    await state.reset_state()

    try:
        await bot.send_message(chat_id=user_id, text=text)
    except Exception:
        logging.info('Mailing error!!!')

    await message.answer(f'Рассылка пользователю с id {user_id} выполнена')
