from aiogram import types
from aiogram.types import ContentType

from loader import dp


@dp.message_handler(content_types=ContentType.PHOTO)
async def get_file_id_photo(message: types.Message):
    await message.reply(message.photo[-1].file_id)
