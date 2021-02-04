from aiogram.dispatcher.filters.state import StatesGroup, State


# Ask question state
class ReportBug(StatesGroup):
    ReportText = State()
    UserName = State()
    UserPhoneNumber = State()
    UserEmail = State()
    Finish = State()

    @staticmethod
    def class_name():
        return 'ReportBug'
