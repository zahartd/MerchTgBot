import logging
import typing

from aiogram import types
from aiogram.dispatcher import FSMContext

from data import states_main_menu
from loader import dp
from states import states_list


@dp.message_handler(text='Выйти 🔙', state=states_list)
@dp.message_handler(text='Отмена ❌', state=states_list)
async def cancel(message: types.Message, state: FSMContext):
    curr_state: str = await state.get_state()
    main_state_name: str = curr_state.split(':')[0]
    menu_to_back_func = states_main_menu.states_main_menu[main_state_name]
    await state.reset_state()
    await menu_to_back_func(message)
