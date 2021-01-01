from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.merch_keyboards import item_keyboard
from loader import dp
from utils.db_api.db_commands import get_item
from utils.db_api.schemas.items import Item


@dp.message_handler(Command('shirt_hb'))
async def bot_start(message: types.Message):
    # Get keyboard
    markup = item_keyboard(3, level=1)

    # Get Item
    item: Item = await get_item(3)

    # Take a record about our product from the database
    await message.answer_photo(item.photos[0],
                               caption=f'{item.name}\nЦена: {item.price} руб.',
                               reply_markup=markup)
