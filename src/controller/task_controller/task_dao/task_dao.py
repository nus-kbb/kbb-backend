from sqlalchemy import text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy import create_engine
import os

class TaskDao: 
    taskTabName = "task_table"
    user = os.getenv("db_user")
    pwd = os.getenv("db_password")
    host = os.getenv("localhost")
    db = "kbb_db"
    dbUrl = f"mysql+pymysql://{user}:{pwd}@{host}/{db}"
    engine = create_engine(dbUrl)
    Session = sessionmaker(bind=engine)
    
    def __init__(self) -> None:
        pass
    
    def CreateTaskEntry(self, task):
        with self.engine.connect() as conn:
            conn.execute(text(f"INSERT INTO  {self.db}.{self.taskTabName} (`project_id`, `user_id`, `status`, `content`) VALUES ({task.project_id},  {task.user_id},  '{task.status.value}',  '{task.content}')"))
            conn.commit()
    