#!/usr/bin/python3
import MySQLdb
from sys import argv

def main():
    # Unpack arguments
    mysql_username, mysql_password, database_name, state_name_searched = argv[1:]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user="root",
                         password="Florent", db="hbtn_0e_0_usa")

    # Create a cursor object
    cur = db.cursor()

    # Create the SQL query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the SQL query
    cur.execute(query, (state_name_searched,))

    # Fetch all the results
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cur.close()
    db.close()

if __name__ == "__main__":
    main()