from utils.db_api.db_commands import get_user
from utils.db_api.schemas.users import User


async def checkout(user_id: int) -> str:
    # Get user
    user: User = await get_user(user_id)

    # Generate email message text
    message_text: str = f'Новый заказ: \nОт: {user.name}\nНомер телефона: {user.phone_number}\nEmail: {user.email}\n'
    for i in range(len(user.basket_name)):
        message_text += f'{i + 1}) Товар # {user.basket_name[i]}\nКоличесто: {user.basket_count[i]}\n'
    message_text += f'------------\n'
    message_text += f'Общая стоимость: {user.total_price}'

    return message_text


async def ask_question(user_id: int, question_text: str, question_subject: str) -> str:
    # Get user
    user: User = await get_user(user_id)

    # Generate email message text
    message_text: str = f'Новый вопрос: \n'\
                        f'От: {user.name}\n'\
                        f'Номер телефона: {user.phone_number}\n'\
                        f'Email: {user.email}\n' \
                        f'Тема вопроса: {question_subject}\n'\
                        f'Текст вопроса: \n{question_text}'

    return message_text


async def report_bug(user_id: int, report_text: str) -> str:
    # Get user
    user: User = await get_user(user_id)

    # Generate email message text
    message_text: str = f'Новое сообщение об ошибке: \n'\
                        f'От: {user.name}\n'\
                        f'Номер телефона: {user.phone_number}\n'\
                        f'Email: {user.email}\n' \
                        f'Описание ошибки: {report_text}\n'

    return message_text


def checking_email(checking_code: str) -> str:
    message_text: str = f'Ваш код подтверждения для заказа в боте РДШ: {checking_code}\n' \
                        f'Скопируйте код и пришлите его боту для окончания формления заказа.'

    return message_text
