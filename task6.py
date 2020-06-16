import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = 'root',
    passwd = '123qwe',
    database = 'PyDB_Demo'
)

my_cursor = mydb.cursor()

my_cursor.execute("drop table employees")
