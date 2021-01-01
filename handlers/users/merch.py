from typing import Union
from aiogram.dispatcher.filters import Command
from aiogram import types

from handlers.users import show_main_menu
from keyboards.inline.merch_keyboards import items_keyboard, menu_cd, item_keyboard
from loader import dp
from utils.db_api.db_commands import get_item


# Show catalog of merch
from utils.db_api.schemas.items import Item


@dp.message_handler(text='Мерч')
@dp.message_handler(text='Мерч 👑')
@dp.message_handler(text='Продолжить покупки 🛍')
@dp.message_handler(Command('merch'))
async def show_catalog(message: types.Message):
    # Show main menu
    await show_main_menu(message)

    # Show list of merch
    await list_items(message)


# Show the main menu
async def to_main_menu(callback: types.CallbackQuery, **kwargs):
    await callback.message.delete()
    await show_main_menu(callback.message)


# Show list of buttons of merch items
async def list_items(message: Union[types.CallbackQuery, types.Message], **kwargs):
    # Get keyboard
    markup = await items_keyboard()

    # Check what kind of update it is. If Message - send a new message
    if isinstance(message, types.Message):
        await message.answer(text=f'Выберете мерч из списка: ', reply_markup=markup)

    # If CallbackQuery - change this message
    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.delete()
        await call.message.answer(text=f'Выберете мерч из списка:', reply_markup=markup)


# Show the item info, photo, buy button
async def show_item(callback: types.CallbackQuery, item_id):
    # Get keyboard
    markup = item_keyboard(item_id)

    # Delete list of items message
    await callback.message.delete()

    # Take a record about our item from the database
    item: Item = await get_item(item_id)

    # Show photo, info and buy button
    await callback.message.answer_photo(item.photos[0],
                                        caption=f'{item.name}\nЦена: {item.price} руб.',
                                        reply_markup=markup)


# Merch list menu navigation
@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):
    """
    :param call: The type of the CallbackQuery object that arrives in the handler
    :param callback_data: Dictionary with data stored in the pressed button
    """

    # Get the current menu level that the user requested
    current_level: str = callback_data.get('level')

    # Get the ID of the item that the user has chosen (It is NOT ALWAYS transmitted - it can be 0)
    item_id: int = int(callback_data.get('item_id'))

    # Register the "levels" in which new buttons will be sent to the user
    levels: dict = {
        '0': to_main_menu,  # Go to main menu
        '1': list_items,  # Give goods
        '2': show_item  # Give item
    }

    # Take away the desired function for the selected level
    current_level_function = levels[current_level]

    # Perform the desired function and pass the parameters received from the button there
    await current_level_function(call, item_id=item_id)
