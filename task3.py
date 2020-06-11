import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = 'root',
    passwd = '123qwe',
    database = 'PyDB_Demo'
)

my_cursor = mydb.cursor()

my_cursor.execute("SELECT * FROM employees WHERE Salary>18000")

result =my_cursor.fetchall()


for record in result:
    print('Emp ID:', record[0])
    print('Full name:', record[1], record[2])
    print('Email:', record[3])
    print('Job Title', record[4])
    print('Hire Date', record[5])
    print('Salary', record[6])
    print('**********************************')

    query = "SELECT * FROM employees WHERE EmpId<10 AND Job_Title LIKE 'w%'"
my_cursor.execute(query)

result = my_cursor.fetchall()
print("----------------------------------------------------")

for data in result:
    print('Emp ID:', data[0])
    print('Full name:', data[1], data[2])
    print('Email:', data[3])
    print('Job Title', data[4])
    print('Hire Date', data[5])
    print('Salary', data[6])


print('==========================================================')


query = "SELECT * FROM employees WHERE first_name LIKE 'R%' OR last_name LIKE '%J'"
my_cursor.execute(query)
example = my_cursor.fetchall()

for data in example: 
    print('Emp ID:', data[0])
    print('Full name:', data[1], data[2])
    print('Email:', data[3])
    print('Job Title', data[4])
    print('Hire Date', data[5])
    print('Salary', data[6])
    print('####################')


query = "SELECT * FROM employees WHERE Hire_Date > '2008-12-15'"
my_cursor.execute(query)
example2 = my_cursor.fetchall()

for data in example2: 
    print('Emp ID:', data[0])
    print('Full name:', data[1], data[2])
    print('Email:', data[3])
    print('Job Title', data[4])
    print('Hire Date', data[5])
    print('Salary', data[6])
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')