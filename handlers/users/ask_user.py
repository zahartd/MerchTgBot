import logging
from typing import Union, Optional
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroupMeta
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove


async def ask_user(message: types.Message, state: Optional[StatesGroupMeta] = None, text: str = '...',
                   markup: Union[ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove, None] = None,
                   back: bool = False):
    await message.answer(text=f'{text}', reply_markup=markup)
    if state:
        if back:
            state_position: str = await state.previous()
        else:
            state_position: str = await state.next()
        state_position = state_position.removeprefix(f'{state.class_name()}:')
        await getattr(state, state_position).set()
        logging.info(state)
