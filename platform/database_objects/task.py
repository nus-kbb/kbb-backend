from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from config_local import postgres_url

from .user import User
from .project import Project

Base = declarative_base()
engine = create_engine(postgres_url)
Session = sessionmaker(bind=engine)


class Task(Base):
    __tablename__ = "task_table"
    id = Column(Integer, primary_key=True)
    project_id = Column(String, ForeignKey(Project.id), unique=True) 
    # TODO relationship with project and user
    user_id = Column(String, ForeignKey(User.id))
    status = Column(String)
    content = Column(String)
    created_on = Column(DateTime(timezone=True),server_default=func.now())


Base.metadata.create_all(engine) # Line to initialize the database