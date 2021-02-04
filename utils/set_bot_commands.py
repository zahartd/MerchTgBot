from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('help', 'Список доступных команд'),
        types.BotCommand('menu', 'Главное меню'),
        types.BotCommand('merch', 'Посмотреть мерч РДШ'),
        types.BotCommand('shirt', 'Купить футболку РДШ'),
        types.BotCommand('polo', 'Купить поло РДШ'),
        types.BotCommand('istand', 'Купить информационный стенд РДШ'),
        types.BotCommand('cstand', 'Купить обычный стенд РДШ'),
        types.BotCommand('spyder', 'Купить стенд-паук РДШ'),
        types.BotCommand('badges', 'Купить значок РДШ'),
        types.BotCommand('flag', 'Купить флаг (большой) РДШ'),
        types.BotCommand('bracelet', 'Купить браслет РДШ'),
        types.BotCommand('notebook', 'Купить блокнот РДШ'),
        types.BotCommand('basket', 'Корзина товаров'),
        types.BotCommand('checkout', 'Оформить заказ'),
        types.BotCommand('edit_basket', 'Редактировать корзину'),
        types.BotCommand('events', 'Посмотреть будущие мероприятия РДШ'),
        types.BotCommand('info', 'Посмотреть информацию об РДШ'),
        types.BotCommand('list', 'Посмотреть топ активных школ'),
        types.BotCommand('ask', 'Задать вопрос РДШ'),
        types.BotCommand('report', 'Сообщить об ошибке')
    ])
