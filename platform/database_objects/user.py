# https://helloworldtest.atlassian.net/wiki/spaces/NUSKBB/pages/4423681/Entity+Relation+Diagram

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy import create_engine

from config_local import local_mysql_url, local_host, local_user, local_passwd, local_database

from project import Project

Base = declarative_base()

engine = create_engine(local_mysql_url)
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True)
    user_email = Column(String(100), unique=True) 
    project_id = Column(Integer, ForeignKey(Project.id))
    # TODO relationship with project
    user_password = Column(String(100))
    created_on = Column(DateTime(timezone=True),server_default=func.now())
    
# CRUD operations - WIP (Just an example - might be moved to DAO)
def get_user():
    try:
        session = Session()
        session.delete()
        session.commit()
    finally:
        session.close()

def update_user():
    try:
        session = Session()
        session.delete()
        session.commit()
    finally:
        session.close()

def delete_user():
    try:
        session = Session()
        session.delete()
        session.commit()
    finally:
        session.close()

# For testing purposes
def delete_all_user():
    try:
        session = Session()
        all = session.query().all()
        return all
    finally:
        pass

Base.metadata.create_all(engine) # Line to initialize the database

print('User table created!')