from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Create edit basket menu
edit_basket_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Удалить позицию ❌'),
        ],
        [
            KeyboardButton(text='Редактировать позицию ✏'),
        ],
        [
            KeyboardButton(text='Очистить корзину 🎇'),
        ],
        [
            KeyboardButton(text='Выйти 🔙')
        ]
    ],
    resize_keyboard=True
)


def position_keyboard(pos_cnt: int):
    markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

    for i in range(pos_cnt):
        button = KeyboardButton(text=f'{i + 1}')
        markup.insert(button)

    return markup

