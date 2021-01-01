import logging

from loader import db
from utils import set_default_commands
from utils.db_api import database, add_goods


async def on_startup(dispatcher):
    import filters
    import middlewares
    filters.setup(dispatcher)
    middlewares.setup(dispatcher)

    logging.info('Connect to DB')
    await database.on_startup(dispatcher)

    # Only for first start
    # # Create table
    # logging.info('Create tables')
    # await db.gino.drop_all()
    # await db.gino.create_all()
    #
    # # Add goods
    # logging.info('Add goods to database')
    # await add_goods.add_items()

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dispatcher)
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
