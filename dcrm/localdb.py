import psycopg2
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

def database():
    conn = psycopg2.connect(
      host=os.environ.get('DATABASE_HOST'),
      database=os.environ.get('DATABASE_NAME'),
      user=os.environ.get('DATABASE_USERNAME'),
      password=os.environ.get('DATABASE_PASSWORD'),
    )
    return conn

# prepare a cursor object
cursorObject = database().cursor()

# execute the SQL query
cursorObject.execute("SELECT * FROM dcrm")

# fetch all data from the cursor
rows = cursorObject.fetchall()

# print rows
for row in rows:
    print(row)

cursorObject.close()

# close the connection
database().close()