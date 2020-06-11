import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = 'root',
    passwd = '123qwe'
)
print(mydb)

my_cursor = mydb.cursor()
my_cursor.execute('SHOW DATABASES')

print(my_cursor)

for db in my_cursor:
    print(db)

#below line is commited because once I create database and for running again and againg it will give me error 
#my_cursor.execute('CREATE DATABASE PyDB_Demo')

my_cursor.execute('USE PyDB_Demo')
# adding table
my_cursor.execute("CREATE TABLE IF NOT EXISTS employees (EmpId int primary key auto_increment, first_name VARCHAR(40), last_name VARCHAR(40), email VARCHAR(50), Job_Title VARCHAR(40), Hire_Date date, Salary decimal check ( salary >= 15000 AND salary <=50000))")

#to see the table we created
my_cursor.execute('SHOW TABLES')
for table in my_cursor:
    print(table)


