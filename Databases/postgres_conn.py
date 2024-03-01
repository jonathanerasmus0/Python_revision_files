# psycopg2
# psycopg2-binary

import psycopg2


db_name = "postgres"
db_host = "localhost"
db_user = "postgres"
db_password = "Lancaster017!"

try:
    db_connections = psycopg2.connect(
        database=db_name,
        user=db_user,
        password=db_password,
        host=db_host
    )
except Exception as error:
    print(error)
else:
    print("Database connection successful")