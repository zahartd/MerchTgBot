from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


# Show information about organisation
@dp.message_handler(text='Будущие мероприятия')
@dp.message_handler(text='Будущие мероприятия 🔮')
@dp.message_handler(Command('events'))
async def print_future_events(message: types.Message):
    await message.answer(text=f'Будущие мероприятия РДШ: ')
    await message.answer(text=f'📍 с 10 по 31 января\nОбновленный проект "Контент на коленке"\nПрием заявок на сайте РДШ\nhttps://рдш.рф/competition/269')
    await message.answer(text=f'📍 4 января - 24 января\nКонкурс "Страницы Великой Победы" в рамках зимнего этапа #РДШ_ВПН\nhttps://vk.com/wall-122623791_231950')
    await message.answer(text=f'📍С 4 по 28 февраля\nДо 15 февраля крайний день заявочного этапа, Зимний этап Всероссийского конкурса "Экологическая культура" Всероссийского проекта "Экотренд",\nhttps://vk.com/wall-134213803_26514')
    await message.answer(text=f'📍с 1 декабря по 30 января\nВсероссийский проект "Я познаю Россию. Прогулки по стране"')
    await message.answer(text=f'📍14.01.21 в 15:00\nПрямой эфир "Открытый космос",\nhttps://vk.com/naukardsh?w=wall-194440650_2183')
