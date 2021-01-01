from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Create main checkout menu (one button - Cancel)
checkout_menu_main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отмена ❌'),
        ]
    ],
    resize_keyboard=True
)

# Create main checkout menu (two button - Cancel and GetPhone)
checkout_menu_phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отправить мой номер телефона 📞', request_contact=True),
        ],
        [
            KeyboardButton(text='Отмена ❌'),
        ]
    ],
    resize_keyboard=True
)
