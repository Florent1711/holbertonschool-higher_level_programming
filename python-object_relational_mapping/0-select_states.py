import MySQLdb

def list_states(username, password, database):
    # Connect to the MySQL server
    conn = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cur = conn.cursor()

    # Execute the query to get all states
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch the results
    results = cur.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()

# Call the function with the arguments
list_states('username', 'password', 'hbtn_0e_0_usa')