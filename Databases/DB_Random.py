import psycopg2
import random

# Database connection parameters, with error handling and security best practices
db_params = {
    "host": "localhost",  # Consider using environment variables for sensitive data
    "dbname": "postgres",  # Change to your desired database name
    "user": "postgres",    # Change to your actual database user
    "password": "Lancaster017!",  # Use a complex password
    "port": "5432"
}

try:
    # Connect to the database
    conn = psycopg2.connect(**db_params)

except psycopg2.Error as e:
    print(f"Error connecting to database: {e}")
    raise

else:
    print("Connected to database successfully!")

    with conn:  # Use context manager for automatic resource management

        # Create a cursor
        cur = conn.cursor()

        # Check if database exists to avoid errors
        try:
            cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_params['dbname'],))
            exists = cur.fetchone()[0]
        except psycopg2.Error as e:
            print(f"Error checking database existence: {e}")
            raise

        if not exists:
            try:
                cur.execute("CREATE DATABASE RandomPeopleDB")
                print("Created database RandomPeopleDB successfully!")
            except psycopg2.Error as e:
                print(f"Error creating database: {e}")
                raise

        # Update db_params to connect to the new database
        db_params["dbname"] = "RandomPeopleDB"

        # Reconnect to the new database
        try:
            conn = psycopg2.connect(**db_params)
            print("Connected to RandomPeopleDB successfully!")
        except psycopg2.Error as e:
            print(f"Error connecting to RandomPeopleDB: {e}")
            raise

        with conn:

            # Create cursors for efficient execution
            cur_men = conn.cursor()
            cur_women = conn.cursor()

            # Create tables with proper data types and constraints
            try:
                cur_men.execute("""
                    CREATE TABLE men (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        age SMALLINT CHECK (age >= 18 AND age <= 87) NOT NULL,
                        city VARCHAR(50) NOT NULL
                    )
                """)

                cur_women.execute("""
                    CREATE TABLE women (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        age SMALLINT CHECK (age >= 18 AND age <= 87) NOT NULL,
                        city VARCHAR(50) NOT NULL
                    )
                """)

                print("Tables created successfully!")
            except psycopg2.Error as e:
                print(f"Error creating tables: {e}")
                raise

            # Generate and insert random data using parameterized queries
            men_data = []
            women_data = []
            for i in range(1, 13):
                name = f"Male{i}"
                age = random.randint(18, 87)
                city = f"City{random.randint(1, 10)}"
                men_data.append((name, age, city))
                women_data.append((f"Female{i}", age, city))

            try:
                # Perform insertions efficiently with executemany
                cur_men.executemany("INSERT INTO men (name, age, city) VALUES (%s, %s, %s)", men_data)
                cur_women.executemany("INSERT INTO women (name, age, city) VALUES (%s, %s, %s)", women_data)

                print("Data inserted successfully!")
            except psycopg2.Error as e:
                print(f"Error inserting data: {e}")
                raise

    # Close cursors and commit changes (if using separate cursors)
    if cur_men:
        cur_men.close()
    if cur_women:
        cur_women.close()
    conn.commit()

finally:
    # Close connection (even if there's an error)
    if conn:
        conn.close()

print("Disconnected from database.")

