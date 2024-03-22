#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port="3306",
                         user="root",
                         passwd="Florent",
                         db="hbtn_0e_0_usa")
    c = db.cursor()
    c.execute("""SELECT * FROM states
              WHERE name LIKE BINARY "N%"
              ORDER BY id ASC""")
    result = c.fetchall()
    for row in result:
        print(row)
    c.close()