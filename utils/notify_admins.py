import logging

from aiogram import Dispatcher

from data.config import admins
from keyboards.default import main_menu


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Бот Запущен", reply_markup=main_menu)

        except Exception as err:
            logging.exception(err)
