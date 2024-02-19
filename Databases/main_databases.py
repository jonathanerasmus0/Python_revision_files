import psycopg2

# Establishing a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="Lancaster017!",
    port="5432"
)

# Creating a cursor object using the connection
cur = conn.cursor()

# Creating the 'person' table if it doesn't exist already
cur.execute("""
    CREATE TABLE IF NOT EXISTS person (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        gender CHAR
    );
""")

# Inserting data into the 'person' table
cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
                (12,'jonathan', 52, 'm'),
                (23,'peter', 43, 'm'),
                (22,'joatan', 5, 'm'),
                (17,'petr', 43, 'm'),
                (9,'joan', 76, 'w');
            """)

# Selecting data from the 'person' table based on name
cur.execute("""SELECT * FROM person WHERE name = 'joan';""")
print(cur.fetchone())

# Selecting data from the 'person' table based on age
cur.execute("""SELECT * FROM person WHERE age > 5;""")
print(cur.fetchall())

# Using mogrify to construct the SQL statement with parameters
sql = cur.mogrify("""SELECT * FROM person WHERE name LIKE %s AND age > %s;""", ('j%', 5))
print(sql)

# Executing the SQL statement
cur.execute(sql)
print(cur.fetchall())

# Committing the transaction
conn.commit()

# Closing the cursor and the connection
cur.close()
conn.close()
