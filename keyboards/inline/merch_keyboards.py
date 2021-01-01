from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.db_api.db_commands import get_items

# Create CallbackData objects for the work with the menu
menu_cd = CallbackData('show_menu', 'level', 'item_id')
buy_item = CallbackData('buy', 'item_id')
order_name = CallbackData('order_name', 'update')


# Form a callback date for each menu item
def make_callback_data(level: int, item_id: int = 0):
    return menu_cd.new(level=level, item_id=item_id)


# Give a keyboard with available items
async def items_keyboard(level: int = 1):
    CURRENT_LEVEL = level

    # Set row_width = 1 to show one button per row per item
    markup = InlineKeyboardMarkup(row_width=1)

    # Take a list of goods from the database
    items = await get_items()
    for item in items:
        # Form the button text
        button_text = f"{item.name} {item.emodji}"

        # Form a button callback data
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, item_id=item.id)
        markup.insert(
            InlineKeyboardButton(
                text=button_text, callback_data=callback_data
            )
        )

    # Create a Back button
    markup.row(
        InlineKeyboardButton(
            text='Назад 🔙',
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1)
        )
    )
    return markup


# Give a keyboard with "buy" and "back" buttons for the selected item
def item_keyboard(item_id, level: int = 2):
    CURRENT_LEVEL = level
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text=f'Добавить в корзину ➕',
            callback_data=buy_item.new(item_id=item_id)
        ),
        InlineKeyboardButton(
            text='Назад 🔙',
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1)
        )
    )
    return markup
