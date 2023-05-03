import os
from src.dao.databaseDAO import *
from src.dto.project_dto.project_dto import Project
class ProjectDAO(DBDAO):

    table = "project_table"
    user_table = 'user_table'

    def __init__(self) -> None:
        super().__init__(table_name=self.table)
        self.session = self.getSession()
        self.engine = self.getEngine()

    def create_project(self, project):
        with self.engine.connect() as conn:
            try:
                result = conn.execute(text(f"INSERT INTO  {local_database}.{self.table} (`project_name`, `status`, `content`) VALUES ('{project.project_name}',  '{project.status}',  '{project.content}')"))
                conn.commit()
                # Because can only create 1 item
                project.id = result.lastrowid
                return project.to_dict()
            except Exception as e:
                return e

    # def get_all_user(self):
    #     with self.engine.connect() as conn:
    #         results = conn.execute(text(f"SELECT * FROM  {local_database}.{self.table}")).all()
    #         _user = []
    #         for it in results:
    #             user = User.from_dict(it._mapping)
    #             _user.append(user.to_dict())
    #         return _user
    def get_project_id_by_name(self, project_name):
        with self.engine.connect() as conn:
            try:
                results = conn.execute(text(f"SELECT id from {local_database}.{self.table} WHERE project_name='{project_name}'"))
                for r in results:
                    return r._mapping["id"]
                return "project name not found"
            except Exception as e:
                return e
    def get_all_project(self):
        with self.engine.connect() as conn:
            try:
                results = conn.execute(text(f"SELECT * FROM {local_database}.{self.table}"))
                conn.commit()
                projectList = []
                for r in results:
                    projectList.append(dict(r._mapping))
                return projectList
            except Exception as e:
                return e

    def get_project_by_userID(self, userID):
        with self.engine.connect() as conn:
            results = conn.execute(text(f"SELECT {local_database}.{self.table}.* " 
                                        f"FROM  {local_database}.{self.table} " 
                                        f"JOIN {local_database}.{self.user_table} " 
                                        f"ON {local_database}.{self.table}.id = {local_database}.{self.user_table}.project_id " 
                                        f"WHERE {local_database}.{self.user_table}.id ='{userID}'")).all()
            
            # Since project is unique, we can return the first result
            if len(results) == 0:
                return None
            else:
                print(dict(results[0]._mapping))
                #project = Project.from_dict(results[0]._mapping)
                return dict(results[0]._mapping)
    def update_project_by_projectID(self, id, project):
        with self.engine.connect() as conn:
            try:
                result = conn.execute(text(f"UPDATE {local_database}.{self.table} \
                                           SET project_name = '{project.project_name}', \
                                           status = '{project.status}', \
                                           content = '{project.content}' \
                                           WHERE id = '{id}'"))
                conn.commit()
                return project.to_dict()
            except Exception as e:
                return e
        
    def delete_project_by_projectID(self, projectID):
        with self.engine.connect() as conn:
            try: 
                #print(text(f"DELETE FROM {local_database}.{self.table} WHERE id = '{projectID}'"))
                conn.execute(text(f"DELETE FROM {local_database}.{self.table} WHERE id = '{projectID}'"))
                conn.commit()
                return "Success"
            except Exception as e:
                return e