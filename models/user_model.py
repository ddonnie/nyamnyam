from sqlalchemy import Column, String, Integer
from sqlalchemy import UniqueConstraint

from models.base import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)

    def __init__(self, username):
        self.username = username