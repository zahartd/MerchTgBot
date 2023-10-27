from aiogram.dispatcher.filters.state import StatesGroup, State


class Mailing(StatesGroup):
    TextEveryOne = State()
    TextProjects = State()
    TextOne = State()
    ID = State()

    @staticmethod
    def class_name():
        return 'Mailing'
