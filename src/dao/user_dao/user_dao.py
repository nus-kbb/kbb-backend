import os
from src.dao.databaseDAO import *
from src.dto.user.user_dto import User
class UserDAO(DBDAO):

    table = "user_table"

    def __init__(self) -> None:
        super().__init__(table_name=self.table)
        self.session = self.getSession()
        self.engine = self.getEngine()

    def create_user(self, user):
        with self.engine.connect() as conn:
            try:
                result = conn.execute(text(f"INSERT INTO  {local_database}.{self.table} (`user_email`, `user_password`, `project_id`) VALUES ('{user.user_email}',  '{user.user_password}',  '{user.project_id}')"))
                conn.commit()
                # Because can only create 1 item
                user.id = result.lastrowid
                return user.to_dict()
            except Exception as e:
                return e

    def get_all_user(self):
        with self.engine.connect() as conn:
            results = conn.execute(text(f"SELECT * FROM  {local_database}.{self.table}")).all()
            list = []
            for it in results:
                user = User.from_dict(it._mapping)
                list.append(user.to_dict())
            return list
        
    def get_user_by_userEmail(self, userEmail):
        with self.engine.connect() as conn:
            results = conn.execute(text(f"SELECT * FROM  {local_database}.{self.table} WHERE user_email='{userEmail}'")).all()
            # Since user is unique, we can return the first result
            if len(results) == 0:
                return None
            else:
                user = User.from_dict(results[0]._mapping)
                return user.to_dict()
        
    def update_user_by_userEmail(self, userEmail, user):
        with self.engine.connect() as conn:
            try:
                result = conn.execute(text(f"UPDATE {local_database}.{self.table} SET user_password = '{user.user_password}', project_id = '{user.project_id}' WHERE user_email = '{userEmail}'"))
                conn.commit()
                # Don't understand the result here
                # if len(result.all()) == 0:
                #     return None
                # return result.all()
                return user.to_dict()
            except Exception as e:
                return e
        
    def delete_user_by_userEmail(self, userEmail):
        with self.engine.connect() as conn:
            try: 
                conn.execute(text(f"DELETE FROM {local_database}.{self.table} WHERE user_email = '{userEmail}'"))
                conn.commit()
                return "Success"
            except Exception as e:
                return e