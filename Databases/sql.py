import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root"
	

)
print(mydb)

my_cursor = mydb.cursor()
# previous step was to CREATE A DATABASE
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
	print(db)
 