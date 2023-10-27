from sqlalchemy import (Column, String, Sequence, BigInteger, Integer)
from sqlalchemy import sql
from utils.db_api.database import db


# Create a users table class
class User(db.Model):
    __tablename__ = 'users'

    # Unique User ID
    id: int = Column(BigInteger, Sequence('user_id_seq'), primary_key=True)
    nickname: str = Column(String(100))  # User nickname
    username: str = Column(String(100))  # User name
    name: str = Column(String(100))  # User real name
    referral: int = Column(Integer)  # User referral
    query: sql.Select
