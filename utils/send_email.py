import logging

from data.config import EMAIL_PASSWORD, EMAIL_FROM, EMAIL_TO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


# Send email
async def send_email(message_text: str, email_subject: str, email_to: str):
    """
    :param email_to: str; Email address to send
    :param email_subject: Email subject
    :param message_text: Text of message to send
    :return: None; Send email with information of order
    """

    # Create sending object
    msg = MIMEMultipart()

    # Setup the parameters of the message
    password: str = EMAIL_PASSWORD
    msg['From']: str = EMAIL_FROM
    msg['To']: str = email_to
    msg['Subject']: str = email_subject

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
