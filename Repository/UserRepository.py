from Repository.AbstractRepository import AbstractRepository
from Models.User import User

class UserRepository(AbstractRepository):

    table_name = 'users'
    item_obj = User