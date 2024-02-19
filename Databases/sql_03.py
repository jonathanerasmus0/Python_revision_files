import psycopg2

# Establishing a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="Lancaster017!",
    port="5432"
)

cur=conn.cursor()
cur.execute (""" CREATE TABLE IF NOT EXISTS person(
			id INT PRIMARY KEY,
			name VARCHAR(255),
			age INT,
			gender CHAR
);
             
             
             
             """)




conn.commit()
# Closing the cursor and the connection
cur.close()
conn.close()