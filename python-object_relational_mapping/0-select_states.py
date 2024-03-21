#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="Angelina1711", db="hbtn_0e_0_usa")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
