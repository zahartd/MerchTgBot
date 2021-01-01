from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove

from handlers.users import show_main_menu
from loader import dp
from utils.db_api.db_commands import add_user


@dp.message_handler(CommandStart(deep_link=None))
async def bot_start(message: types.Message):
    # Get user full name
    name: str = message.from_user.full_name

    # Get user ID
    user_id: int = message.from_user.id

    # Add user to database
    await add_user(user_id=user_id, name=name)

    # Show main menu
    await message.answer(text=f'Привет, {name}!')
    await show_main_menu(message)
