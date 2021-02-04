from sqlalchemy import (Column, Integer, String, Sequence, ARRAY)
from sqlalchemy import sql
from utils.db_api.database import db


# Create a goods table class
class Item(db.Model):
    __tablename__ = 'items'

    # Unique goods ID
    id: int = Column(Integer, Sequence('user_id_seq'), primary_key=True)

    # Name, photo and price of goods
    name: str = Column(String(50))
    emodji: str = Column(String(50))
    photos: list = Column(ARRAY(item_type=String))
    price: int = Column(Integer)
    category_name: str = Column(String(50))
    category_code: str = Column(String(20))
    subcategory_name: str = Column(String(50))
    subcategory_code: str = Column(String(20))

    query: sql.Select

    def __repr__(self):
        return f"""Товар № {self.id} - "{self.name}\nЦена: {self.price}"""
