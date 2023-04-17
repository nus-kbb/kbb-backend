# Steps on how to create the database tables
## 1. How to create a virtual environment and activate the environment
- For MacOS
  - Navigate to where you want to store your code. Create new directory.
    - mkdir my_project && cd my_project
    - INSIDE my_project folder create a new virtualenv
    - virtualenv env_kbb
  - Activate virtualenv
    - source env/bin/activate


- Using the requirements.txt file, to install all packages
    - pip install -r /path/to/requirements.txt

## 2. Connection string to the local database
- Create a config_local.py file in database_objects folder
- Use the following string for your localhost, replace it with your postgres username and password
- postgres_url = "postgresql://<user>:<password>@localhost:5432/kbb_db"

## 3. Creating of the Database tables
- cd to the folder of the database_objects folder
- run each individual python file to create the database in your local machine