from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Create main poll menu
poll_menu_main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отмена ❌'),
        ]
    ],
    resize_keyboard=True
)

# Create first poll menu
poll_menu_first = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отмена ❌'),
        ]
    ],
    resize_keyboard=True
)

# Create main poll menu
poll_menu_optionally = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Далее ⏭'),
        ],
        [
            KeyboardButton(text='Отмена ❌'),
        ]
    ],
    resize_keyboard=True
)

# Create main checkout menu (two button - Cancel and GetPhone)
poll_menu_phone = ReplyKeyboardMarkup(
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
