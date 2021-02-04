from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import MediaGroup

from data import items_command
from keyboards.inline.merch_keyboards import item_keyboard
from loader import dp
from utils.db_api.db_commands import get_item
from utils.db_api.schemas.items import Item


@dp.message_handler(Command('shirt'))
@dp.message_handler(Command('polo'))
@dp.message_handler(Command('istand'))
@dp.message_handler(Command('cstand'))
@dp.message_handler(Command('spyder'))
@dp.message_handler(Command('badges'))
@dp.message_handler(Command('flag'))
@dp.message_handler(Command('bracelet'))
@dp.message_handler(Command('notebook'))
async def show_item_command(message: types.Message):
    category: str = items_command[message.text]['category']
    item_id: int = items_command[message.text]['item_id']

    # Get keyboard
    markup = item_keyboard(category, item_id)
    album = MediaGroup()

    # Take a record about our item from the database
    item: Item = await get_item(item_id)
    photos = item.photos

    for photo in photos:
        album.attach_photo(photo)

    await message.answer_media_group(media=album)
    await message.answer(text=f'{item.name}\nЦена: {item.price} руб.', reply_markup=markup)
