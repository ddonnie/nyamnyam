from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

association_table = Table(
    'users_places', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.user_id')),
    Column('place_id', Integer, ForeignKey('places.place_id'))

)


class Place(Base):
    __tablename__ = 'places'

    place_id = Column(Integer, primary_key=True)
    placename = Column(String)
    users = relationship("User", secondary=association_table)

    def __init__(self, placename, users):
        self.placename = placename
        self.users = users
