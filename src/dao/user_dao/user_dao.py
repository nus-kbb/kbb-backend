import os
from src.dao.databaseDAO import DBDAO
from environment.database_objects.user import User
class UserDAO(DBDAO):

    def __init__(self) -> None:
        super().__init__( "user_table")
        self.session = self.getSession()

    def create_user(self, user):
        return user

    def get_all_user(self):
        # result = self.session.query(User).all()
        result = []
        return result