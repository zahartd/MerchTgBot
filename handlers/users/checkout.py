import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from handlers.users import show_goods_basket, show_main_menu
from keyboards.default.checkout_menu import checkout_menu_main, checkout_menu_phone
from loader import dp
from states import Checkout
from utils.db_api.db_commands import get_user, update_user_order_name, update_user_phone_number, update_user_basket, \
    update_user_total_price
from utils.db_api.schemas.users import User

from data.config import EMAIL_PASSWORD, EMAIL_FROM, EMAIL_TO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


# Forming text about user order to email sending
async def form_email_message_text(user_id: int) -> str:
    # Get user
    user: User = await get_user(user_id)

    # Generate email message text
    message_text: str = f'Новый заказ: \nОт: {user.order_name}\nНомер телефона: {user.phone_number}\n'
    for i in range(len(user.basket_name)):
        message_text += f'{i + 1}) Товар # {user.basket_name[i]}\nКоличесто: {user.basket_count[i]}\n'
    message_text += f'------------\n'
    message_text += f'Общая стоимость: {user.total_price}'

    return message_text


# Clean user goods basket
async def clean_basket(user_id: int):
    """
    :param user_id: User ID
    :return: None; Clean user goods basket
    """

    # Clean basket columns
    await update_user_basket(user_id, basket_name=[], basket_count=[])

    # Zero total price in basket
    await update_user_total_price(user_id, total_price=0)

    logging.info('Successfully clear basket!')


# Send email with information of order
async def send_email(message_text: str):
    """
    :param message_text: Text of message to send
    :return: None; Send email with information of order
    """

    # Create sending object
    msg = MIMEMultipart()

    # Setup the parameters of the message
    password: str = EMAIL_PASSWORD
    msg['From']: str = EMAIL_FROM
    msg['To']: str = EMAIL_TO
    msg['Subject']: str = "Новый заказ"

    # Add text in the message body
    msg.attach(MIMEText(message_text, 'plain'))

    # Create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    # Start server
    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # Send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    # Quit server
    server.quit()

    logging.info(f'Successfully sent email to {msg["To"]}')


# Request user name
async def request_user_name(message: types.Message):
    await message.answer(text=f'Укажите ваше реальное имя: ',
                         reply_markup=checkout_menu_main)
    await Checkout.UserName.set()


# Request client phone number
async def request_phone_number(message: types.Message):
    await message.answer(text=f'Укажите номер телефона, чтобы мы могли связаться с вами: ',
                         reply_markup=checkout_menu_phone)
    await Checkout.UserPhoneNumber.set()


# Start checkout order
@dp.message_handler(text='Оформить заказ')
@dp.message_handler(text='Оформить заказ ✅')
@dp.message_handler(Command('checkout'))
async def start_checkout_order(message: types.Message):
    # Request user name
    await request_user_name(message)


# Get client name, commit it to database and request user phone number
@dp.message_handler(state=Checkout.UserName)
async def get_user_name(message: types.Message, state: FSMContext):
    if message.text != 'Отмена ❌':  # Check to cancel checkout or continue
        # Get user ID
        user_id: int = message.from_user.id

        # Get client name and add it to state
        async with state.proxy() as data:
            data['client_name']: str = message.text

        # Commit it to database
        await update_user_order_name(user_id, data['client_name'])

        # Request phone number
        await request_phone_number(message)
    else:  # Else return to basket
        await state.reset_state()
        await show_goods_basket(message, state)


# Get user phone number and send information about order
@dp.message_handler(state=Checkout.UserPhoneNumber, content_types=types.ContentTypes.CONTACT)
@dp.message_handler(state=Checkout.UserPhoneNumber, content_types=types.ContentTypes.TEXT)
async def get_user_phone_number(message: types.Message, state: FSMContext):
    # Get user ID
    user_id: int = message.from_user.id

    # Get user phone number
    # Check for types
    async with state.proxy() as data:
        if message.content_type == 'CONTACT':
            data['phone_number']: str = message.contact.phone_number
        else:
            data['phone_number']: str = message.text

    # Check for correct input data
    if (data['phone_number'].isdigit() or (data['phone_number'][1:].isdigit() and data['phone_number'][0] == '+'))\
            and 10 <= len(data['phone_number']) <= 12:
        # Commit it to database
        await update_user_phone_number(user_id, data['phone_number'])

        # Forming email message
        message_text = await form_email_message_text(user_id)

        # Send email
        await send_email(message_text)

        # Clean user basket
        await clean_basket(user_id)

        # Finish state
        await state.finish()

        # Send information about order status to user
        await message.answer(text=f'Ваш заказ принят! Скоро с вами свяжутся')

        # Return to main menu
        await show_main_menu(message)
    else:  # Else request phone number again
        await message.answer(text=f'Упс) Похоже это не номер телефона. '
                                  f'Пожалуйста проверьте корректность введеных данных')
        await request_phone_number(message)
