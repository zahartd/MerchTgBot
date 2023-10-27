from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text: list[str] = [
        'Список команд: ',
        '/start - Начать диалог бота',
        '/help - Список доступных команд',
        '/menu - Главное меню',
        '/merch - Унать подробнее про мерч',
        '/events - Посмотреть будущие мероприятия',
        '/list - Посмотреть информацию',
        '/info - Посмотреть топ активных пользователей',
        '/ask - Задать вопрос'
        '/report - Сообщить об ошибке'
    ]
    await message.answer(text='\n'.join(text))
