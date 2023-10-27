import re
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from handlers.users import show_main_menu
from loader import dp
from utils.db_api.db_commands import add_user, get_user_by_id, update_user_data, get_users_by_project


@dp.message_handler(CommandStart(deep_link=re.compile(r'bsj')))
async def bot_start(message: types.Message):
    # Get user full name
    username: str = message.from_user.username
    full_name: str = message.from_user.full_name

    # Get user ID
    user_id: int = message.from_user.id

    if get_user_by_id(user_id) is None:
        await update_user_data(user_id=user_id, nickname=username, username=full_name)
    else:
        await add_user(user_id=user_id, nickname=username, username=full_name)

    if user_id not in get_users_by_project(project='bsj'):
        await add_user(user_id=user_id, nickname=username, username=full_name)

    # Show main menu
    await message.answer(text=f'Привет, {full_name}, участник проекта <Название организации скрыто> Junior! Бот будет присылать '
                              f'ссылки на трансяцию, домашку и всю остальную информацию.'
                              f' А пока можете посмотреть, что у нас есть)')
    await show_main_menu(message)


@dp.message_handler(CommandStart(deep_link=None))
async def bot_start(message: types.Message):
    # Get user full name
    username: str = message.from_user.username
    full_name: str = message.from_user.full_name

    # Get user ID
    user_id: int = message.from_user.id

    # Add user to database
    await add_user(user_id=user_id, nickname=username, username=full_name)

    # Show main menu
    await message.answer(text=f'Привет, {full_name}!')
    await show_main_menu(message)
