import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()
conn = pyodbc.connect(os.getenv("DB_CONN_STR"))
cursor = conn.cursor()

cursor.execute("SELECT name FROM sys.tables")
print(cursor.fetchall())  # You should see your table names here

cursor.close()
conn.close()
