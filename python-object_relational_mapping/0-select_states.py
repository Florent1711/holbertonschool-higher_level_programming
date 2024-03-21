#!/usr/bin/python3
import MySQLdb
from sys import argv

def list_states(username, password, db_name):
    """
    Lists all states from the database.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(argv) == 4:
        list_states(argv[1], argv[2], argv[3])
