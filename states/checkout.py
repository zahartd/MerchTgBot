from aiogram.dispatcher.filters.state import StatesGroup, State


# Checkout state
class Checkout(StatesGroup):
    UserName = State()
    UserPhoneNumber = State()
    UserSchool = State()
    UserDistrict = State()
    UserEmail = State()
    Finish = State()

    @staticmethod
    def class_name():
        return 'Checkout'
