from environment.database_objects.config import *
from sqlalchemy import text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy import create_engine

class DBDAO:
    Base = declarative_base()
    engine = create_engine(local_mysql_url, future=True)
    session = sessionmaker(bind=engine)
    print("db url", local_mysql_url)
    
    def __init__(self, table_name):
        self.taskTabName = table_name

    def getSession(self):
        return self.session()
    
    def getEngine(self):
        return self.engine
    
    def sqlquote(self, value):
        """Naive SQL quoting

        All values except NULL are returned as SQL strings in single quotes,
        with any embedded quotes doubled.

        """
        if value is None:
            return 'NULL'
        else:
            return "'{}'".format(str(value).replace("'", "''"))