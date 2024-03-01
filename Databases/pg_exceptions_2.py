import psycopg2
from psycopg2 import exceptions

# Connection details
host = "localhost"
database = "my_database"
user = "my_user"
password = "my_password"

try:
  # Connect to the database
  conn = psycopg2.connect(host=host, database=database, user=user, password=password)

  # Execute a sample query
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM non_existent_table")

  # Fetch results (This line might raise an error)
  rows = cursor.fetchall()

  # Process the results (not shown for brevity)

except exceptions.ProgrammingError as error:
  print("Error: Invalid table name. Please check your query.")
  print(f"Details: {error}")

except exceptions.OperationalError as error:
  print("Error: Could not connect to the database. Please check connection details.")
  print(f"Details: {error}")

finally:
  # Close the connection (always essential)
  if conn:
    conn.close()

print("Successfully executed the query (if no errors occurred).")
