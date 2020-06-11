import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = 'root',
    passwd = '123qwe',
# I use below Database for this project
    database = 'PyDB_Demo'
)

my_cursor = mydb.cursor()

sql_query = 'INSERT INTO employees (first_name,last_name,email,Job_Title,Hire_Date,Salary) VALUES (%s,%s,%s,%s,%s,%s)'
# I need to use Python List "Array"

many_record_values = [
    (  'Hasti', 'Amin', 'Hasti@gmail.ca', 'WebDeveloper', '2015-01-01',16000),
    (  'tawheed', 'Ami', 'tawheed@gmail.ca', 'Database administrator', '2010-01-01',19000),
    (  'Rida', 'jalali', 'R.J@gmail.ca', 'WebDeveloper', '2008-12-15',40000),
    (  'Josse', 'jj', 'lo@gmail.ca', 'webdesigner', '2009-04-09',18000),
    (  'Smith', 'ray', 'mm@gmail.ca', 'WebDeveloper', '2014-06-08',45000) 
]

# To insert multiple rows into a table, we use the executemany() method.

my_cursor.executemany(sql_query,many_record_values)

#  commit the code:
mydb.commit()

#  print num of rows added: property "rowcount"
print(my_cursor.rowcount, "row(s) inserted")

print('------------------')
print("result with labels:")
print('------------------')
my_cursor.execute('SELECT * FROM employees')
for record in my_cursor:
    print('Emp ID:', record[0])
    print('Full name:', record[1], record[2])
    print('Email:', record[3])
    print('Job Title', record[4])
    print('Hire Date', record[5])
    print('Salary', record[6])
    print('**********************************')
