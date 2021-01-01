from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text: list[str] = [
        'Список команд: ',
        '/start - Запустить бота',
        '/help - Список доступных команд',
        '/menu - Главное меню',
        '/merch - Унать подробнее и купить мерч от РДШ',
        '   /sweatshirt - Купить свитшот от РДШ',
        '   /bomber - Купить бомбер от РДШ',
        '   /shirt_hb - Купить футболку хб от РДШ',
        '   /shirt_polo - Купить футболку поло от РДШ',
        '/basket - Корзина товаров',
        '/checkout - Оформить заказ',
        '/edit_basket - Редактировать корзину'
        '/list - Посмотреть информацию об РДШ',
        '/info - Посмотреть топ активных школ'
    ]
    await message.answer(text='\n'.join(text))
