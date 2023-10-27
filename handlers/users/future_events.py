from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


# Show information about organisation
@dp.message_handler(text='Будущие мероприятия')
@dp.message_handler(text='Будущие мероприятия 🔮')
@dp.message_handler(Command('events'))
async def print_future_events(message: types.Message):
    await message.answer(text=f'Будущие мероприятия: ')
    await message.answer(text=f'15 февраля стартует проект <>. Все подробности в группе VK.'
                              f' https://vk.com/')
