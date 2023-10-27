from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.db_api.db_commands import get_items, count_items, get_categories

# Create CallbackData objects for the work with the menu
menu_cd = CallbackData('show_menu', 'level', 'category', 'item_id')
buy_item = CallbackData('buy', 'item_id')
order_name = CallbackData('order_name', 'update')


# Form a callback date for each menu item
def make_callback_data(level: int, category='1', item_id: int = 0):
    return menu_cd.new(level=level, category=category, item_id=item_id)


async def categories_keyboard(level: int = 1):
    # Указываем, что текущий уровень меню - 0
    CURRENT_LEVEL = 1

    # Создаем Клавиатуру
    markup = InlineKeyboardMarkup(row_width=1)

    # Забираем список товаров из базы данных с РАЗНЫМИ категориями и проходим по нему
    categories = await get_categories()
    for category in categories:
        # Чекаем в базе сколько товаров существует под данной категорией
        number_of_items = await count_items(category.category_code)

        # Сформируем текст, который будет на кнопке
        button_text = f"{category.category_name} ({number_of_items} шт)"

        # Сформируем колбек дату, которая будет на кнопке. Следующий уровень - текущий + 1, и перечисляем категории
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, category=category.category_code)

        # Вставляем кнопку в клавиатуру
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    return markup


# Give a keyboard with available items
async def items_keyboard(category: str, level: int = 2):
    CURRENT_LEVEL = level

    # Set row_width = 1 to show one button per row per item
    markup = InlineKeyboardMarkup(row_width=1)

    # Take a list of goods from the database
    items = await get_items(category)
    for item in items:
        # Form the button text
        button_text = f"{item.name} {item.emodji}"

        # Form a button callback data
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, category=category, item_id=item.id)
        markup.insert(
            InlineKeyboardButton(
                text=button_text, callback_data=callback_data
            )
        )

    # Create a Back button
    markup.row(
        InlineKeyboardButton(
            text='Назад 🔙',
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1, category=category)
        )
    )
    return markup


# Give a keyboard with "buy" and "back" buttons for the selected item
def item_keyboard(category, item_id, level: int = 3):
    CURRENT_LEVEL = level
    markup = InlineKeyboardMarkup()
    markup.row(
        # InlineKeyboardButton(
        #     text=f'Добавить в корзину ➕',
        #     callback_data=buy_item.new(item_id=item_id)
        # ),
        InlineKeyboardButton(
            text='Назад 🔙',
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1, category=category)
        )
    )
    return markup
