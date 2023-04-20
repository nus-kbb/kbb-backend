from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy import create_engine

class TaskDao: 
    Base = declarative_base()
    engine = create_engine(local_mysql_url)
    Session = sessionmaker(bind=engine)
    
    def __init__(self) -> None:
        pass
    
    def CreateTaskDao:
    