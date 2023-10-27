# import logging
#
# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command
# from aiogram.types import ReplyKeyboardRemove
#
# from data import poll_questions
# from data.config import admins
# from handlers.users import show_main_menu, ask_user, init_getting, get_user_data
# from keyboards.default import poll_menu_first, poll_menu_main
# from loader import dp
# from states import NewItem
#
#
# @dp.message_handler(Command('add_item'), user_id=admins)
# async def start_add_item(message: types.Message, state: FSMContext):
#     await message.answer('Вы вошли в режим добавления нового товара, чтобы выйти нажмите Отмена ❌')
#     await init_getting(message=message, state=state)
#     await ask_user(message=message, state=NewItem,
#                    text=poll_questions['new_item_name'],
#                    markup=poll_menu_first)
#
#
# @dp.message_handler(user_id=admins, state=NewItem.Name)
# async def get_item_name(message: types.Message, state: FSMContext):
#     await get_user_data(message=message, main_state=state, data_name='new_item_name', update_db=False)
#     await ask_user(message=message, state=NewItem, text=poll_questions['new_item_photos'], markup=poll_menu_main)
#
#
# @dp.message_handler(user_id=admins, state=NewItem.Photo)
# async def get_item_photos(message: types.Message, state: FSMContext):
#     await get_user_data(message=message, main_state=state, data_name='new_item_photos', update_db=False)
#     await ask_user(message=message, state=NewItem, text=poll_questions['new_item_price'], markup=poll_menu_main)
#
#
# @dp.message_handler(user_id=admins, state=NewItem.Price)
# async def enter_price(message: types.Message, state: FSMContext):
#     await get_user_data(message=message, main_state=state, data_name='new_item_price', update_db=False)
#     data = await state.get_data()
#     item: Item = data.get("item")
#     try:
#         price = int(message.text)
#     except ValueError:
#         await message.answer(_("Неверное значение, введите число"))
#         return
#
#     item.price = price
#     markup = InlineKeyboardMarkup(
#         inline_keyboard=
#         [
#             [InlineKeyboardButton(text=_("Да"), callback_data="confirm")],
#             [InlineKeyboardButton(text=_("Ввести заново"), callback_data="change")],
#         ]
#     )
#     await message.answer(_("Цена: {price:,}\n"
#                            "Подтверждаете? Нажмите /cancel чтобы отменить").format(price=price / 100),
#                          reply_markup=markup)
#     await state.update_data(item=item)
#     await NewItem.Confirm.set()
#
#
# @dp.callback_query_handler(user_id=admin_id, text_contains="change", state=NewItem.Confirm)
# async def enter_price(call: types.CallbackQuery):
#     await call.message.edit_reply_markup()
#     await call.message.answer(_("Введите заново цену товара в копейках"))
#     await NewItem.Price.set()
#
#
# @dp.callback_query_handler(user_id=admin_id, text_contains="confirm", state=NewItem.Confirm)
# async def enter_price(call: types.CallbackQuery, state: FSMContext):
#     await call.message.edit_reply_markup()
#     data = await state.get_data()
#     item: Item = data.get("item")
#     await item.create()
#     await call.message.answer(_("Товар удачно создан."))
#     await state.reset_state()
