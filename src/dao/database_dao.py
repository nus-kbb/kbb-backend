from sqlalchemy import create_engine
from platform.database_objects.config import local_mysql_url

engine = create_engine(local_mysql_url)