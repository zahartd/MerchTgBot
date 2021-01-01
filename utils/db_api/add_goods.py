from sqlalchemy import ARRAY

from utils.db_api.db_commands import add_item


# Add to database goods
async def add_items():
    await add_item(id=1, name='Свитшот', price=1300,
                   photos=['https://sbis.perm.ru/wp-content/uploads/2019/09/placeholder.png'], emodji='🧥')
    await add_item(id=2, name='Бомбер', price=1600,
                   photos=['https://sbis.perm.ru/wp-content/uploads/2019/09/placeholder.png'], emodji='🥼')
    await add_item(id=3, name='Футболка xб', price=600,
                   photos=['https://sbis.perm.ru/wp-content/uploads/2019/09/placeholder.png'], emodji='👕')
    await add_item(id=4, name='Футболка поло', price=800,
                   photos=['https://sbis.perm.ru/wp-content/uploads/2019/09/placeholder.png'], emodji='👕')
