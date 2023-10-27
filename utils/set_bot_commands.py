from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Начать диалог бота'),
        types.BotCommand('help', 'Список доступных команд'),
        types.BotCommand('menu', 'Главное меню'),
        types.BotCommand('merch', 'Посмотреть будущие мероприятия'),
        types.BotCommand('events', 'Посмотреть будущие мероприятия'),
        types.BotCommand('info', 'Посмотреть информацию об <НОС>'),
        types.BotCommand('list', 'Посмотреть топ активных школ'),
        types.BotCommand('ask', 'Задать вопрос'),
        types.BotCommand('report', 'Сообщить об ошибке')
    ])
