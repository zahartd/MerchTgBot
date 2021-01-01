from asyncpg import UniqueViolationError

from utils.db_api.database import db
from utils.db_api.schemas.items import Item
from utils.db_api.schemas.users import User


# Items commands
# Add a new goods in the database. Accepts all possible arguments specified in Item
async def add_item(**kwargs) -> Item:
    new_item = await Item(**kwargs).create()
    return new_item


# Display all goods
async def get_items() -> list[Item]:
    return await Item.query.distinct(Item.name).gino.all()


# Get a goods object by ID
async def get_item(item_id: int) -> Item:
    item = await Item.query.where(Item.id == item_id).gino.first()
    return item


# Users commands
# Add a new user to database
async def add_user(user_id: int, name: str, basket_name=None, basket_count=None,
                   order_name: str = '', phone_number: str = '', total_price: int = 0):
    if basket_name is None:
        basket_name: list[str] = []
    if basket_count is None:
        basket_count: list[int] = []
    try:
        user = User(id=user_id, name=name, basket_name=basket_name, basket_count=basket_count,
                    order_name=order_name, phone_number=phone_number, total_price=total_price)
        await user.create()
    except UniqueViolationError:
        pass


# Get all user
async def get_all_users() -> list[User]:
    users = await User.query.gino.all()
    return users


# Get user by ID
async def get_user(user_id: int) -> User:
    user = await User.query.where(User.id == user_id).gino.first()
    return user


# Count user
async def count_user() -> int:
    total: int = await db.func.count(User.id).gino.scalar()
    return total


# Update user basket
async def update_user_basket(user_id: int, basket_name: list[str], basket_count: list[int]):
    user = await User.get(user_id)
    await user.update(basket_name=basket_name, basket_count=basket_count).apply()


# Update user order name
async def update_user_order_name(user_id: int, order_name: str):
    user = await User.get(user_id)
    await user.update(order_name=order_name).apply()


# Update user phone number
async def update_user_phone_number(user_id: int, phone_number: str):
    user = await User.get(user_id)
    await user.update(phone_number=phone_number).apply()


# Update user phone number
async def update_user_total_price(user_id: int, total_price: int):
    user = await User.get(user_id)
    await user.update(total_price=total_price).apply()
