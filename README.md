# csv-to-mysql-database
What is MySQL?
MySQL is the world’s most popular open source database. According to DB-Engines, MySQL ranks as the second-most-popular database, behind Oracle Database. MySQL powers many of the most accessed applications, including Facebook, Twitter, Netflix, Uber, Airbnb, Shopify, and Booking.com.

Since MySQL is open source, it includes numerous features developed in close cooperation with users over more than 25 years. So it’s very likely that your favorite application or programming language is supported by MySQL Database.

How do you pronounce “MySQL”?
“My ess-cue-el” is the “official” way to pronounce “MySQL,” but pronouncing it “my sequel” is common too.

What is the name of the MySQL dolphin?
The MySQL logo is a dolphin named Sakila. The name was chosen from a large list suggested by users during the “Name the Dolphin” contest. The winning name was submitted by Ambrose Twebaze, an open source software developer from Eswatini (formerly Swaziland), Africa.

MySQL is a relational database management system
Databases are the essential data repository for all software applications. For example, whenever someone conducts a web search, logs in to an account, or completes a transaction, a database system is storing the information so it can be accessed in the future.

A relational database stores data in separate tables rather than putting all the data in one big storeroom. The database structure is organized into physical files optimized for speed. The logical data model, with objects such as data tables, views, rows, and columns, offers a flexible programming environment. You set up rules governing the relationships between different data fields, such as one to one, one to many, unique, required, or optional, and “pointers” between different tables. The database enforces these rules so that with a well-designed database your application never sees data that’s inconsistent, duplicated, orphaned, out of date, or missing.

The “SQL” part of “MySQL” stands for “Structured Query Language.” SQL is the most common standardized language used to access databases. Depending on your programming environment, you might enter SQL directly (for example, to generate reports), embed SQL statements into code written in another language, or use a language-specific API that hides the SQL syntax.

MySQL is open source
Open source means it’s possible for anyone to use and modify the software. Anybody can download MySQL software from the internet and use it without paying for it. You can also change its source code to suit your needs. MySQL software uses the GNU General Public License (GPL) to define what you may and may not do with the software in different situations.

If you feel uncomfortable with the GNU GPL or need to embed MySQL code into a commercial application, you can buy a commercially licensed version from Oracle. See the MySQL Licensing Information section for more information.

MySQL: the #1 choice for developers
MySQL consistently ranks as the most popular database for developers, according to surveys from Stack Overflow and JetBrains. Developers love its high performance, reliability, and ease of use.

MySQL supports the following popular development languages and drivers:

PHP	Python	Java/JDBC	Node.js
Perl	Ruby	Go	Rust
C	C++	C#/.NET	ODBC
MySQL has also become the database of choice for many of the most successful open source applications, including WordPress, Drupal, Joomla, and Magento. MySQL is the “M” in the highly popular open source LAMP (Linux, Apache, MySQL, Perl/Python/PHP) stack to develop web applications.

MySQL works in client/server or embedded systems
MySQL Database is a client/server system that consists of a multithreaded SQL server that supports different back ends, several different client programs and libraries, administrative tools, and a wide range of application-programming interfaces (APIs). We also provide MySQL as an embedded multithreaded library that you can link into your application to get a smaller, faster, easier-to-manage standalone product.

MySQL benefits
MySQL is fast, reliable, scalable, and easy to use. It was originally developed to handle large databases quickly and has been used in highly demanding production environments for many years.

Although MySQL is under constant development, it offers a rich and useful set of functions. MySQL’s connectivity, speed, and security make it highly suited for accessing databases on the internet.

MySQL’s key benefits include

Ease of use: Developers can install MySQL in minutes, and the database is easy to manage.

Reliability: MySQL is one of the most mature and widely used databases. It has been tested in a wide variety of scenarios for more than 25 years, including by many of the world’s largest companies. Organizations depend on MySQL to run business-critical applications because of its reliability.

Scalability: MySQL scales to meet the demands of the most accessed applications. MySQL’s native replication architecture enables organizations such as Facebook to scale applications to support billions of users.

Performance: MySQL HeatWave is faster and less expensive than other database services, as demonstrated by multiple standard industry benchmarks, including TPC-H, TPC-DS, and CH-benCHmark.

High availability: MySQL delivers a complete set of native, fully integrated replication technologies for high availability and disaster recovery. For business-critical applications, and to meet service-level agreement commitments, customers can achieve

Recovery point objective = 0 (zero data loss)
Recovery time objective = seconds (automatic failover)
Security: Data security entails protection and compliance with industry and government regulations, including the European Union General Data Protection Regulation, the Payment Card Industry Data Security Standard, the Health Insurance Portability and Accountability Act, and the Defense Information Systems Agency’s Security Technical Implementation Guides. MySQL Enterprise Edition provides advanced security features, including authentication/authorization, transparent data encryption, auditing, data masking, and a database firewall.

Flexibility: The MySQL Document Store gives users maximum flexibility in developing traditional SQL and NoSQL schema-free database applications. Developers can mix and match relational data and JSON documents in the same database and application.

MySQL use cases
Cloud applications: MySQL is very popular in the cloud. MySQL HeatWave is a fully managed database service, powered by the integrated HeatWave in-memory query accelerator. It’s the only cloud database service that combines transactions, real-time analytics across data warehouses and data lakes, and machine learning (ML) services into one MySQL Database—without the complexity, latency, cost, and risk of ETL duplication. MySQL HeatWave is 6.5X faster than Amazon Redshift at half the cost, 7X faster than Snowflake at one-fifth the cost, and 1,400X faster than Amazon Aurora at half the cost. With MySQL HeatWave AutoML, developers and data analysts can build, train, deploy, and explain machine learning models within MySQL HeatWave in a fully automated way—25X faster than Amazon Redshift ML at 1% of the cost.

Step 1: Prepare the CSV File
To begin, prepare the CSV file that you'd like to import to MySQL. For example, I prepared a simple CSV file with the following data:

Step 2: Import the CSV File into the DataFrame.
Next, import the CSV file into Python using the pandas library. Here is the code that I used to import the CSV file, and then create the DataFrame. You'll need to change the path name to reflect the location where the CSV file is stored on your computer


import pandas as pd
empdata = pd.read_csv('C:\\Users\\XXXXX\\empdata.csv', index_col=False, delimiter = ',')
empdata.head()

Step 3 : Connect to the MySQL using Python and create a Database
Create a connection object to connect to MySQL, The connect() constructor creates a connection to the MySQL and returns a MySQLConnection object.


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE employee")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)

Note :if you don't connect then, please install the mysql-connector-python package, type the following command:

        pip install mysql-connector-python

Output of the above code: After running the above the code will create an employee database in mysql as shown in below.

Step 4: Create a table and Import the CSV data into the MySQL table
We will create an employee_data table under the employee database and insert the records in MySQL with below python code.
import mysql.connector as msql
from mysql.connector import Error
    try:
        conn = mysql.connect(host='localhost', database='employee', user='root', password='root@123')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            cursor.execute('DROP TABLE IF EXISTS employee_data;')
            print('Creating table....')
       
            
in the below line please pass the create table statement which you want #to create
the connection is not auto committed by default, so we must commit to save our changes

        cursor.execute("CREATE TABLE employee_data(first_name varchar(255),last_name varchar(255),company_name varchar(255),address varchar(255),city varchar(255),county varchar(255),state varchar(255),zip int,phone1 varchar(255),phone2 varchar(255),email varchar(255),web varchar(255))")
        print("Table is created....")
        for i,row in empdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO employee.employee_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)

Step 5 : Query the Table
Query the table to make sure that our inserted data has been saved correctly.


Execute query:

    sql = "SELECT * FROM employee.employee_data"
    cursor.execute(sql)
Fetch all the records
    result = cursor.fetchall()
    for i in result:
        print(i)

Tips for this code:

The problem is that the dataframe contains NaN values; when passed to the query NaN is not quoted because it's a number, but it gets stringified like this

        for i,row in empdata.fillna(-1).iterrows():
            sql="INSERT INTO blood_emploee_tableS3 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,tuple(row))
            # print("Record inserted")
            con.commit()
            
and the database interprets the unquoted "string" as a column name and can't find the column.

The solution is to replace or remove such values before writing to the database, for example by using fillna to replace them with some other, suitable value:

Pandas DataFrame iterrows() Method

The iterrows() method generates an iterator object of the DataFrame, allowing us to iterate each row in the DataFrame.

Each iteration produces an index object and a row object (a Pandas Series object).

      dataframe.iterrows()
