from aiogram.dispatcher.filters.state import StatesGroup, State


# Checkout state
class Checkout(StatesGroup):
    UserName = State()
    UserPhoneNumber = State()
