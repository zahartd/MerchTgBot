from aiogram import Dispatcher
from gino import Gino
from data.config import POSTGRES_URI

db = Gino()


async def on_startup(dispatcher: Dispatcher):
    # Connect to database
    await db.set_bind(POSTGRES_URI)
    # db.gino: GinoSchemaVisitor
