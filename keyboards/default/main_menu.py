from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Create main menu
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Информация ℹ'),
            KeyboardButton(text='Список активных школ 📃'),
        ],
        [
            KeyboardButton(text='Мерч 👑'),
            KeyboardButton(text='Корзина 🧺'),
        ],
        [
            KeyboardButton(text='Cd')
        ]
    ],
    resize_keyboard=True
)
