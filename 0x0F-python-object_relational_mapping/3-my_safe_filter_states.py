#!/usr/bin/python3
""" """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    connector = MySQLdb.Connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cursor = connector.cursor()
    cursor.execute("""SELECT * FROM states WHERE name = %s
                     ORDER BY states.id ASC""", (argv[4], ))
    result = cursor.fetchall()
    for row in result:
        print(row)
