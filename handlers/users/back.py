import logging
import typing

from aiogram import types
from aiogram.dispatcher import FSMContext

from data import poll_questions
from handlers.users import ask_user
from loader import dp
from states import states_list, states_dict


@dp.message_handler(text='Назад 🔙', state=states_list)
async def back_question(message: types.Message, state: FSMContext):
    state_data: dict = await state.get_data()
    prev_question_name: str = state_data['prev_question_name']
    prev_question_markup = state_data['prev_question_markup']
    curr_state: str = await state.get_state()
    main_state_name: str = curr_state.split(':')[0]
    main_state = states_dict[main_state_name]
    await ask_user(message=message, state=main_state, text=poll_questions[prev_question_name],
                   markup=prev_question_markup, back=True)
