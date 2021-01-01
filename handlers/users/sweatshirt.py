from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.merch_keyboards import item_keyboard
from loader import dp
from utils.db_api.db_commands import get_item
from utils.db_api.schemas.items import Item


@dp.message_handler(Command('sweatshirt'))
async def bot_start(message: types.Message):
    # Get keyboard
    markup = item_keyboard(1, level=1)

    # Get Item
    item: Item = await get_item(1)

    # Take a record about our item from the database
    await message.answer_photo(item.photos[0],
                               caption=f'{item.name}\nЦена: {item.price} руб.',
                               reply_markup=markup)
