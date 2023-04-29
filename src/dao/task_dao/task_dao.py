from src.dao.databaseDAO import *
from src.dto.task_dto.task_dto import Task
import os

class TaskDao(DBDAO): 
    table = "task_table"

    def __init__(self) -> None:
        super().__init__(table_name=self.table)
        self.session = self.getSession()
        self.engine = self.getEngine()
        pass
    
    def CreateTaskEntry(self, task):
        with self.engine.connect() as conn:
            try:
                conn.execute(text(f"INSERT INTO  {local_database}.{self.table} (`project_id`, `user_id`, `status`, `content`) VALUES ({task.project_id},  {task.user_id},  '{task.status}',  '{task.content}')"))
                conn.commit()
            except Exception as e:
                print("Error create task: ", e)
                return e.__str__
    
    def UpdateTaskEntry(self, task):
        with self.engine.connect() as conn:
            try:
                conn.execute(text(f"UPDATE {local_database}.{self.table} SET `project_id` = {task.project_id}, `user_id` = {task.user_id}, `status` = '{task.status}', `content` = '{task.content}' WHERE `id` = {task.id}"))
                conn.commit()
            except Exception as e:
                print("Error update task: ", e)
                return e.__str__   

    def DeleteTaskEntry(self, taskId):
        with self.engine.connect() as conn:
            try:
                conn.execute(text(f"DELETE FROM {local_database}.{self.table} WHERE `id` = {taskId}"))
                conn.commit()  
            except Exception as e:
                print("Error delete task: ", e)
                return e.__str__  
    
    def GetAllTask(self):
        with self.engine.connect() as conn:
            try:
                results = conn.execute(text(f"SELECT * FROM  {local_database}.{self.table}")).all()
                taskList = []
                for r in results:
                    taskList.append(Task(**r._mapping).__dict__)
                return taskList
            except Exception as e:
                print("Error getting all task: ", e)
                return e
        
    def GetTaskById(self, id):
        with self.engine.connect() as conn:
            try:
                results = conn.execute(text(f"SELECT * FROM  {local_database}.{self.table} WHERE id = {id}"))
                taskList = []
                for r in results:
                    taskList.append(Task(**r._mapping).__dict__)
                return taskList
            except Exception as e:
                print("Error getting all task: ", e)
                return e
    
    def GetTaskByProjectId(self, projectId):
        with self.engine.connect() as conn:
            try:
                results = conn.execute(text(f"SELECT * FROM  {local_database}.{self.table} WHERE project_id = {projectId}"))
                taskList = []
                for r in results:
                    taskList.append(Task(**r._mapping).__dict__)
                return taskList
            except Exception as e:
                print("Error getting all task: ", e)
                return e
