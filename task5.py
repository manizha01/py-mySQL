import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = 'root',
    passwd = '123qwe',
    database = 'PyDB_Demo'
)

my_cursor = mydb.cursor()

query = "delete from employees WHERE EmpId=3" 

my_cursor.execute(query)

mydb.commit()

my_cursor.execute('SELECT * FROM employees')
for data in my_cursor:
    print('Emp ID:', data[0])
    print('Full name:', data[1], data[2])
    print('Email:', data[3])
    print('Job Title', data[4])
    print('Hire Date', data[5])
    print('Salary', data[6])

print('==========================================================')