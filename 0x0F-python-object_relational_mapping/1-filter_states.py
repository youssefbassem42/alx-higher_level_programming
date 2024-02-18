#!/usr/bin/python3
"""Script for listing all states start with N"""

from sys import argv
import MySQLdb


if __name__ == '__main__':
    connector = MySQLdb.Connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cursor = connector.cursor()
    cursor.execute("SELECT * FROM states WHERE states.name LIKE\
                   BINARY 'N%' ORDER BY states.id ASC")
    result = cursor.fetchall()
    for row in result:
        print(row)
