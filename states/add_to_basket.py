from aiogram.dispatcher.filters.state import StatesGroup, State


# Add to basket state
class AddToBasket(StatesGroup):
    GoodsID = State()
    GoodsName = State()
    Count = State()
    Size = State()
    Price = State()
