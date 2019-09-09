#!/usr/bin/python3

import pymysql
# Open database connection
db = pymysql.connect("localhost","root","","databasename" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
################# read data from table #################
sql = "SELECT * FROM CUSTOMERS \
     WHERE SALARY > '%d'" %(2)
try:
  # Execute the SQL command
  cursor.execute(sql)
  # Fetch all the rows in a list of lists.
  results = cursor.fetchall()
  for row in results:
     ID = row[0]
     NAME = row[1]
     AGE = row[2]
     ADDRESS = row[3]
     SALARY = row[4]
     # Now print fetched result
     print ("ID = %s,NAME = %s,AGE = %d,ADDRESS = %s,SALARY = %d" % \
        (ID, NAME, AGE, ADDRESS, SALARY ))
except:
  print ("Error: unable to fetch data")


################# Creating Database Table #################

## Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS VIP2")

# Create table as per requirement
sql = """CREATE TABLE VIP2 (
  ID INT NOT NULL,  
  JOIN_DATE DATETIME NOT NULL,
  INCOME FLOAT )"""

cursor.execute(sql)

################ INSERT TO TABLE #################

sql = """INSERT INTO VIP2(ID,
   JOIN_DATE, INCOME)
   VALUES ('2', '2017-08-19 22:08:22', 70000)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()