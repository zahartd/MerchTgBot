from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Create item nav menu
item_nav_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Корзина 🧺'),
        ],
        [
            KeyboardButton(text='Продолжить покупки 🛍'),
        ],
        [
            KeyboardButton(text='Главное меню 🕹')
        ]
    ],
    resize_keyboard=True
)
