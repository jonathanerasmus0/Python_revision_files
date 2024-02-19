import psycopg2

# Establishing a connection to the PostgreSQL database
db = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="Lancaster017!",
    port="5432"
)

mycursor = db.cursor()

# Drop the existing 'person' table if it exists
mycursor.execute("DROP TABLE IF EXISTS person")

# Recreate the 'person' table
mycursor.execute("CREATE TABLE person (name VARCHAR(50), age smallint, personId SERIAL PRIMARY KEY)")

# Committing the transaction
db.commit()

# Closing the cursor and the connection
mycursor.close()
db.close()





