from dotenv import load_dotenv
import os
load_dotenv()

# Use os.getenv() to access the environment variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

DATABASE_CONNECTION=f"mysql+pymysql:/{db_user}:{db_password}@{db_host}/{db_name}?charset=utf8mb4"