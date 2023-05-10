# https://helloworldtest.atlassian.net/wiki/spaces/NUSKBB/pages/4423681/Entity+Relation+Diagram

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy import create_engine

from config import local_mysql_url

Base = declarative_base()

print(local_mysql_url)
engine = create_engine(local_mysql_url)
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True)
    user_email = Column(String(100), unique=True)
    project_id = Column(Integer)
    role=Column(String(100))
    # TODO relationship with project
    user_password = Column(String(100))
    created_on = Column(DateTime(timezone=True),server_default=func.now())

Base.metadata.create_all(engine) # Line to initialize the database

print('User table created!')