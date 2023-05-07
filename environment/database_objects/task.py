from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from config import local_mysql_url

from user import User
from project import Project

Base = declarative_base()
engine = create_engine(local_mysql_url)
Session = sessionmaker(bind=engine)

class Task(Base):
    __tablename__ = "task_table"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey(Project.id)) 
    # TODO relationship with project and user
    user_id = Column(Integer, ForeignKey(User.id))
    status = Column(String(100))
    type = Column(String(100))
    story_points = Column(Integer)
    version = Column(String(100))
    content = Column(String(100))
    created_on = Column(DateTime(timezone=True),server_default=func.now())

Base.metadata.create_all(engine) # Line to initialize the database
print('Task table created')