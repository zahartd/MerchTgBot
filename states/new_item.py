from aiogram.dispatcher.filters.state import StatesGroup, State


class NewItem(StatesGroup):
    Name = State()
    Photo = State()
    Price = State()
    Category = State()
    SubCategory = State()
    Confirm = State()

    @staticmethod
    def class_name():
        return 'NewItem'
