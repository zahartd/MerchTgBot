from aiogram.dispatcher.filters.state import StatesGroup, State


# Ask question state
class AskQuestion(StatesGroup):
    QuestionText = State()
    QuestionSubject = State()
    UserName = State()
    UserPhoneNumber = State()
    UserEmail = State()
    Finish = State()

    @staticmethod
    def class_name():
        return 'AskQuestion'
