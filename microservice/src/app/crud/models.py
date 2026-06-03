from crud.base import BaseService
from models.items import Items
from models.users import Users

class ItemsDAO(BaseService):
    model = Items

class UsersDAO(BaseService):
    model = Users