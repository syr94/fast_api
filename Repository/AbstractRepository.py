from typing import TypeVar, Generic
from sqlalchemy.orm import Session
T = TypeVar('T')
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import sys

class AbstractRepository:

    table_name = ''
    item_obj = Generic[T]

    def __init__(self) -> None:
        try:
            self.engine = create_engine('postgresql://unsjmswb:Myo0dN8PiMa5P-kYiKZ53bAhYYvlH5Lm@john.db.elephantsql.com/unsjmswb')
            Base = declarative_base()
            Base.metadata.create_all(self.engine)
        except:
            print("Error with database connection, please check conecction config or smthg else")
            e = sys.exc_info()[1]
            print(e.args[0])

    def add(self, object_item = Generic[T]) -> None:
        with Session(self.engine) as session:
            try:
                session.begin() # transaction
                session.add(object_item)  # INSERT into (table_name) values ...
                session.commit()
            except:
                session.rollback()
                print("Somethg wrong happend")
                e = sys.exc_info()[1]
                print(e.args[0])

    def update(self, object_item = Generic[T]) -> None:
        with Session(self.engine) as session:
            try:
                session.begin()
                session.merge(object_item)  # INSERT into (table_name) values ...
                session.commit()
            except:
                session.rollback()
                print("Somethg wrong happend")
                e = sys.exc_info()[1]
                print(e.args[0])
    
    def find_one_by(self, by = "", value = "") -> None:
        with Session(self.engine) as session:
            try:
                session.begin()
                return session.query(self.item_obj).filter(getattr(self.item_obj, by) == value).first()        
            except:
                session.rollback()
                print("Somethg wrong happend")
                e = sys.exc_info()[1]
                print(e.args[0])
    
    def find_all_by(self,  object_item = Generic[T], by = "", value = "") -> None:
        with Session(self.engine) as session:
            try:
                session.begin()
                return session.query(self.item_obj).filter(getattr(self.item_obj, by) == value).all()
            except:
                session.rollback()
                print("Somethg wrong happend")
                e = sys.exc_info()[1]
                print(e.args[0])

