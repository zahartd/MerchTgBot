from aiogram.dispatcher.filters.state import StatesGroup, State


# Add to basket state
class AddToBasket(StatesGroup):
    Count = State()
    Size = State()
    Finish = State()

    @staticmethod
    def class_name():
        return 'AddToBasket'
