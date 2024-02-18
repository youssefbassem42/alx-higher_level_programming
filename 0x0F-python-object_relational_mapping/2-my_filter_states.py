#!/usr/bin/python3
""" Script for ORM Manipulate :

"""

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
    query = """SELECT * FROM states WHERE name
                    LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query.format(argv[4])
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
