from typing import Optional, Union

from aiogram import types
from aiogram.dispatcher import FSMContext


async def init_getting(message: types.Message, state: FSMContext):
    user_id: int = message.from_user.id
    async with state.proxy() as data:
        data['user_id'] = user_id
        data['update_db']: list = []


async def get_user_data(message: Union[types.CallbackQuery, types.Message], main_state: FSMContext, data_name: str,
                        callback_data: Optional[dict] = None, data_type: type = str, update_db: bool = True):
    async with main_state.proxy() as data:
        if isinstance(message, types.Message):
            if message.content_type == 'contact':
                data[data_name]: data_type = data_type(message.contact.phone_number)
            else:
                data[data_name]: data_type = data_type(message.text)
        elif isinstance(message, types.CallbackQuery):
            data[data_name]: data_type = data_type(callback_data.get(data_name))

        if data[data_name] == 'Далее ⏭':
            data[data_name] = 'Не указана'

        if update_db:
            data['update_db'].append(data_name)
