#!/usr/bin/python3

import MySQLdb
import sys

# Connect to the MySQL database
db = MySQLdb.connect(
   host="localhost",
   port=3306,
   user=sys.argv[1],
   passwd=sys.argv[2],
   db=sys.argv[3]
)

# Create a cursor object
cursor = db.cursor()

# Build the query using parameterized formatting to prevent SQL injection
state_name = sys.argv[4]
sql = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

# Execute the query
cursor.execute(sql, (state_name,))

# Fetch and display the results
rows = cursor.fetchall()
for row in rows:
   print(row)

# Close the cursor and database connection
cursor.close()
db.close()
