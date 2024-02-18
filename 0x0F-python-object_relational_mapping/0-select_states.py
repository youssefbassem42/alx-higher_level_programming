#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""
from sys import argv
import MySQLdb as db


if __name__ == '__main__':

    db_connect = db.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
    db_connect.close()
