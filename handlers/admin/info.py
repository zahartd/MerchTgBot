from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import admins
from load_all import dp, _, bot
from states import NewItem, Mailing
from database import Item, User