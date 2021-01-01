from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('help', 'Список доступных команд'),
        types.BotCommand('menu', 'Главное меню'),
        types.BotCommand('merch', 'Посмотреть мерч РДШ'),
        types.BotCommand('sweatshirt', 'Купить свитшот от РДШ'),
        types.BotCommand('bomber', 'Купить бомбер от РДШ'),
        types.BotCommand('shirt_hb', 'Купить футболку хб от РДШ'),
        types.BotCommand('shirt_polo', 'Купить футболку поло от РДШ'),
        types.BotCommand('basket', 'Корзина товаров'),
        types.BotCommand('checkout', 'Оформить заказ'),
        types.BotCommand('edit_basket', 'Редактировать корзину'),
        types.BotCommand('info', 'Посмотреть информацию об РДШ'),
        types.BotCommand('list', 'Посмотреть топ активных школ')
    ])
