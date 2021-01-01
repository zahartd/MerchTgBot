from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Create basket menu
basket_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Оформить заказ ✅'),
        ],
        [
            KeyboardButton(text='Редактировать корзину ✏'),
        ],
        [
            KeyboardButton(text='Главное меню 🕹')
        ]
    ],
    resize_keyboard=True
)
