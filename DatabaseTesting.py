import mysql.connector

#Used to initially connect to the database management system
#Specify the host, user, password, and the database
mydb = mysql.connector.connect(
  host="localhost",
  user="picklemustard",
  password="Purple14735#",
  database="mydatabase"
)

#Creates a cursor object to interact with the database
#This will be used to execute queries within the DBMS
mycursor = mydb.cursor()

#Creates a database within the DBMS
#mycursor.execute("CREATE DATABASE mydatabase")  

#CREATING TABLES
#NOTE: Need to remember the different types of variables avaialbe to SQL languages
#Executes the query to create a table
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255) , address VARCHAR(255))")
#To change a table's headers, use ALTER
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#DELETING TABLES
#Executes the query to delete an existing table
#sql = "DROP TABLE customers"
#mycursor.execute(sql)
#If unsure if the table is already deleted, use IF EXISTS to avoid errors
#sql = "DROP TABLE IF EXISTS customers"
#mycursor.execute(sql)

#JOINING TABLES
#
#sql = "SELECT \
#  users.name AS user, \   (Take the column of name from users and join to new table as user)
#  products.name AS favorite \ (Take the column of name from products and join to new table as favorite)
#  FROM users \  
#  INNER JOIN products ON users.fav = products.id"
#****This joins the specified fields together in a new table that is returned, on INNER JOIN, only the rows that have matching users.fav and products.id
#are put in the new table, on RIGHT JOIN, all rows from the table that is joining(products) will be shown, even if they don't have a matching value, on
#LEFT JOIN, all rows from the table that is being joined(users) will be shown, even if they don't have a matching value
#mycursor.execute(sql)
#myresult = mycursor.fetchall()
#for x in myresult:
#    print(x)

#mycursor.execute("SHOW TABLES")

#INSERTING INTO TABLES ---------------------------------
#This inserts a single row of values into the table
#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("Biden", "Highway 21")
#mycursor.execute(sql, val)

#This inserts multiple rows of values into the table
#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = [('Peter', 'Lowstreet 4'), ('Amy', 'Apple St 652'), ('Hannah', 'Mountain 21'), ('Sandy', 'Ocean Blvd 2')]
#mycursor.executemany(sql, val)

#SELECTING FROM TABLES --------------------------------------------
#Use the SELECT Query | The WHERE statement followed by a column name = 'what to find' allows pinpointing the desired field; can use % to represent wildcard characters
#like %way% which is any field that contains the word way preceded and followed by anything
#Assign the results from the query to a new variable
#For loop the variable
#For Select, can use ORDER BY column_name to order the results in ascending order of the specified column or ORDER BY column_name DESC for it to be in
#descending order
#For Select, can use LIMIT # statement at the end of a query to limit the number of records returned, to change the starting position of where records
#are returned from, use LIMIT # OFFSET #, Ex. LIMIT 5 OFFSET 2 returns 5 entries starrting from position 3

#Select all records
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#The fetchone() method returns the first row of the result
#****NOTE****
#This is done after the fetchall() above but not after an executed query, so the mycursor object has nothing,
#Query results are not retained
myresult = mycursor.fetchone()
print(myresult)

#Select Columns
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
  
#Preventing Injection
#Good practice to escape the values of any query
#Instead of allowing the user to write directly into the query, perform some inspection on the entered values before querying it
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2")
mycursor.execute(sql,adr)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
  
#DELETING FROM TABLES--------------------------------------------
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)

#Preventing Injection
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2")
mycursor.execute(sql,adr)

#UPDATING TABLE VALUES--------------------------------------------
sql = "UPDATE customers STE address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
  
#****IMPORTANT*****
#The .commit() command is required to makes changes to the table, otherwise no changes are made to the table
#It is needed for Creating table values, deleting table values, and updating table values
mydb.commit()

#Prints the number of rows inserted, deleted, or modified
print(mycursor.rowcount, "Rows")

#Prints the ID of the last inserted row
#print("1 record inserted, ID: ", mycursor.lastrowid)


#Can print the database connection object to get information on the database connection
#Gives the memory location of the object
#print(mydb)

#When executing a query that will return values, they will be stored in the cursor object
#It can then be printed to get the values returned
#mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

