# string to configure the database connection - localhost (will have to change to cloud in the future)
# Database parameters for local MySQL database
local_host = "localhost"         
local_user = "root"          
local_passwd = ""    
local_database = "kbb_db"


local_mysql_url = f"mysql+pymysql://root:<insert_password>@localhost/kbb_db"
# local_mysql_url = f"mysql+pymysql://{local_user}:{local_passwd}@{local_host}/{local_database}"