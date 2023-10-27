import logging
from typing import Any, Union
from aiogram import types, Bot

from sqlalchemy import and_
from utils.db_api.schemas.users import User


from asyncpg import UniqueViolationError

from utils.db_api.database import db
from utils.db_api.schemas.items import Item


# Items commands
# Add a new goods in the database. Accepts all possible arguments specified in Item
async def add_item(**kwargs) -> Item:
    new_item = await Item(**kwargs).create()
    return new_item


# Get categories
async def get_categories() -> list[Item]:
    return await Item.query.distinct(Item.category_code).gino.all()


# Get subcategories
async def get_subcategories(category) -> list[Item]:
    return await Item.query.distinct(Item.subcategory_name).where(Item.category_code == category).gino.all()


# Get all items
async def get_items(category_code: str, subcategory_code: str = None) -> list[Item]:
    item = await Item.query.where(Item.category_code == category_code).gino.all()
    return item


async def count_items(category_code: str, subcategory_code=None):
    conditions = [Item.category_code == category_code]

    if subcategory_code:
        conditions.append(Item.subcategory_code == subcategory_code)

    total = await db.select([db.func.count()]).where(
        and_(*conditions)
    ).gino.scalar()
    return total


# Get item by ID
async def get_item(item_id: int) -> Item:
    item = await Item.query.where(Item.id == item_id).gino.first()
    return item


# Users commands
# Add a new user to database
async def add_user(user_id: int, nickname: str, username: str, basket_name=None, basket_count=None,
                   basket_item_price=None, name: str = '', phone_number: str = '', total_price: int = 0, referral=None,
                   projects=None, bsj: int = 0):
    if basket_name is None:
        basket_name: list[str] = []
    if basket_count is None:
        basket_count: list[int] = []
    if basket_item_price is None:
        basket_item_price: list[int] = []
    if referral is None:
        referral: int = -1
    if projects is None:
        projects: list[str] = []
    try:
        user = User(id=user_id, nickname=nickname, username=username, basket_name=basket_name, basket_count=basket_count,
                    basket_item_price=basket_item_price, name=name, phone_number=phone_number, total_price=total_price,
                    referral=referral, projects=projects, bsj=bsj)
        await user.create()
    except UniqueViolationError:
        pass


async def check_referrals(self, user_id: int):
    bot = Bot.get_current()
    user: User = await get_user_by_id(user_id)

    referrals = await User.query.where(user.referral == user_id).gino.all()

    return ", ".join([
        f"{num + 1}. " + (await bot.get_chat(referral.user_id)).get_mention(as_html=True)
        for num, referral in enumerate(referrals)
    ])


# Get categories
async def get_projects() -> list[str]:
    return await User.query.distinct(User.projects).gino.all()


# Get all user
async def get_all_users() -> list[User]:
    users = await User.query.gino.all()
    return users


# Get user by ID
async def get_user_by_id(user_id: int) -> User:
    user = await User.query.where(User.id == user_id).gino.first()
    return user


# Get user by project
async def get_users_by_project(project: str) -> list[User]:
    users = await User.query.gino.all()
    project_user: list[User] = []
    for user in users:
        if project in getattr(user, 'projects'):
            project_user.append(user)

    return project_user


# Count user
async def count_users() -> int:
    total: int = await db.func.count(User.id).gino.scalar()
    return total


async def get_user_database_data(user_id: int, data_name: str) -> Union[str, int, list, tuple, dict]:
    # Get user
    user: User = await get_user_by_id(user_id)

    return getattr(user, data_name)


# Update user data
async def update_user_data(user_id: int, **kwargs):
    # Get user
    user: User = await User.get(user_id)

    # Update user data
    await user.update(**kwargs).apply()


async def get_basket_size(user_id: int, **kwargs) -> int:
    basket: list[str] = await get_user_database_data(user_id, data_name='basket_name')
    basket_size: int = len(basket)

    return basket_size
