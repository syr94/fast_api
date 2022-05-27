from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key = True)
    user_name = Column(String)
    user_email = Column(String)

    def __init__(self, user_id, user_name, user_email):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email
