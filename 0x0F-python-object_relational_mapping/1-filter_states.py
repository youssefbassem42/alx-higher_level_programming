#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    connector = MySQLdb.Connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cursor = connector.cursor()
    cursor.execute("SELECT * FROM states WHERE states.name LIKE\
                   BINARY 'N%' ORDER BY states.id ASC ")
    result = cursor.fetchall()
    for row in result:
        print(row)
