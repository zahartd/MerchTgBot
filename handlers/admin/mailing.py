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


# Фича для рассылки по юзерам (учитывая их язык)
from utils.db_api.schemas.users import User


@dp.message_handler(Command('tell_everyone'), user_id=admins)
async def start_everyone_mailing(message: types.Message):
    await message.answer('Пришлите текст рассылки: ')
    await Mailing.Text.set()


@dp.callback_query_handler(user_id=admins, state=Mailing.Text)
async def mailing_start(message: types.Message, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    await state.reset_state()

    users = await User.gino.all()
    for user in users:
        try:
            await bot.send_message(chat_id=user.user_id, text=text)
            await sleep(0.3)
        except Exception:
            pass
    await message.answer('Рассылка выполнена')
