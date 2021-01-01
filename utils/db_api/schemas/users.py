from sqlalchemy import (Column, String, Sequence, ARRAY, BigInteger, Integer)
from sqlalchemy import sql
from utils.db_api.database import db


# Create a users table class
class User(db.Model):
    __tablename__ = 'users'

    # Unique User ID
    id: int = Column(BigInteger, Sequence('user_id_seq'), primary_key=True)

    name: str = Column(String(100))  # Username
    basket_name: list[str] = Column(ARRAY(String))  # User current goods name in basket
    basket_count: list[int] = Column(ARRAY(Integer))  # User current goods count in basket
    order_name: str = Column(String(100))  # User order
    phone_number: str = Column(String(20))  # User phone number
    total_price: int = Column(BigInteger)  # User basket total price

    query: sql.Select

    def __repr__(self):
        text = f'Корзина пользователя № {self.id} - "{self.name}: \n'
        for i in range(len(self.basket_name)):
            text += f'  {i + 1}) {self.basket_name[i]} x {self.basket_count[i]} шт.\n'
        return text
