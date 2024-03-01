import psycopg2




connection = psycopg2.connect(dbname="postgres", user="postgres", password="Lancaster017!", host="localhost")
cursor = connection.cursor()



select_query = '''
    SELECT * FROM person;

INSERT INTO person (id,name, age, gender)
VALUES ('1111','John', '50', 'm');'''


cursor.execute(select_query)
connection.commit()
##data =cursor.fetchall()
#print(data)