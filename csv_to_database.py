import pandas as pd
# Next, import the CSV file into Python using the pandas library. Here is the code that I used to import the CSV file, and then create the DataFrame. You'll need to change the path name to reflect the location where the CSV file is stored on your computer
empdata = pd.read_csv('C:\\Users\\peyman\\Downloads\\Compressed\\archive\\bloodtypes.csv')
print(empdata.head())
print(empdata)
#///////////////////////////////////////////////////////////////////////////////////////////////
# """Create a connection object to connect to MySQL, The connect() constructor creates a connection to the MySQL and returns a MySQLConnection object."""
import mysql.connector as msql
from mysql.connector import Error
# try:
#     con = msql.connect(host='127.0.0.1',user='root',password='peiman2012')
#     if con.is_connected():
#         cursor = con.cursor()
#         cursor.execute("create database blood_emploee")
#         print("Databases is created....")
#
# except Error as e :
#     print("Error while connecting to MYSQL",e)
# ////////////////////////////////////////////////////////////////////////////////////
# We will create an employee_data table under the employee database and insert the records in MySQL with below python code

try:
    con = msql.connect(host='127.0.0.1',
                       user='root',
                       password='',
                       database='blood_emploee'
                       )
    if con.is_connected():
        cursor=con.cursor()
        cursor.execute("select database();")
        record=cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('drop table if exists blood_emploee_tableS3;')
        print('Creating table....')
        cursor.execute("create table blood_emploee_tableS3 (country char(50) not null, Population char(20) not null,`O+` float not null,`A+` float not null ,`B+` float not null ,`AB+` float not null ,`O-` float not null ,`A-` float not null ,`B-` float not null,`AB-` float not null )")
        print("Table is created....")

        for i,row in empdata.fillna(-1).iterrows():
            sql="INSERT INTO blood_emploee_tableS3 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,tuple(row))
            # print("Record inserted")
            con.commit()
except Error as e :
    print("Error while connecting to MYSQL",e)

# //////////////////////////////////////////////////////////////////////////////////////////////////
# We will create an employee_data table under the employee database and insert the records in MySQL with below python code.

sql = "SELECT * FROM blood_emploee_tableS3 "
cursor.execute(sql)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)



con.close()