from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy import create_engine

from config_local import local_mysql_url

Base = declarative_base()
engine = create_engine(local_mysql_url)
Session = sessionmaker(bind=engine)

class Project(Base):
    __tablename__ = "project_table"
    id = Column(Integer, primary_key=True)
    project_name = Column(String(100), unique=True)
    status = Column(String(100))
    content = Column(String(100))
    created_on = Column(DateTime(timezone=True),server_default=func.now())

Base.metadata.create_all(engine) # Line to initialize the database
print('Project table created')