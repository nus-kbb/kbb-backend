from environment.database_objects.config import local_mysql_url
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy import create_engine

class DBDAO:
    Base = declarative_base()
    engine = create_engine(local_mysql_url)
    session = sessionmaker(bind=engine)
    print("db url", local_mysql_url)
    
    def __init__(self, table_name):
        self.taskTabName = table_name

    def getSession(self):
        return self.session()