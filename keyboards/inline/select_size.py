from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


# Create CallbackData objects for the work with the menu
clothes_size = CallbackData('clothes_size', 'size')


# Give a keyboard with size of clothes
def sizes_keyboard():
    markup = InlineKeyboardMarkup()

    markup.row(
        InlineKeyboardButton(
            text=f'XS/42',
            callback_data=clothes_size.new(size='XS/42')
        ),
        InlineKeyboardButton(
            text='S/44',
            callback_data=clothes_size.new(size='S/44')
        )
    )

    markup.row(
        InlineKeyboardButton(
            text=f'M/46',
            callback_data=clothes_size.new(size='M/46')
        ),
        InlineKeyboardButton(
            text='L/48',
            callback_data=clothes_size.new(size='L/48')
        )
    )

    markup.row(
        InlineKeyboardButton(
            text=f'XL/50',
            callback_data=clothes_size.new(size='XL/50')
        ),
        InlineKeyboardButton(
            text='2XL/52',
            callback_data=clothes_size.new(size='2XL/52')
        )
    )

    return markup
