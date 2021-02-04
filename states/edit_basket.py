from aiogram.dispatcher.filters.state import StatesGroup, State


class EditBasketDeletePos(StatesGroup):
    Position = State()
    Finish = State()

    @staticmethod
    def class_name():
        return 'EditBasketDeletePos'


class EditBasketEditPos(StatesGroup):
    Position = State()
    Count = State()
    Finish = State()

    @staticmethod
    def class_name():
        return 'EditBasketEditPos'
