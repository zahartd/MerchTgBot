from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Create main menu
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Будущие мероприятия 🔮'),
        ],
        [
            KeyboardButton(text='Информация ℹ'),
            KeyboardButton(text='Список активных школ 📃'),
        ],
        [
            KeyboardButton(text='Мерч 👑'),
        ],
        [
            KeyboardButton(text='Задать вопрос 📧')
        ],
        [
            KeyboardButton(text='Сообщить об ошибке в боте 📍')
        ]
    ],
    resize_keyboard=True
)
