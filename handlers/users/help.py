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
        '/shirt - Купить футболку РДШ',
        '/polo - Купить поло РДШ',
        '/istand - Купить информационный стенд РДШ',
        '/cstand - Купить обычный стенд РДШ',
        '/spyder - Купить стенд-паук РДШ',
        '/badges - Купить значок РДШ'
        '/flag - Купить флаг (большой) РДШ',
        '/bracelet - Купить браслет РДШ',
        '/notebook - Купить блокнот РДШ',
        '/basket - Корзина товаров',
        '/checkout - Оформить заказ',
        '/edit_basket - Редактировать корзину',
        '/events - Посмотреть будущие мероприятия РДШ',
        '/list - Посмотреть информацию об РДШ',
        '/info - Посмотреть топ активных школ',
        '/ask - Задать вопрос РДШ'
        '/report - Сообщить об ошибке'
    ]
    await message.answer(text='\n'.join(text))
