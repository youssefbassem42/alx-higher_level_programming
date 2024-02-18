#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
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
    cursor.execute("SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})
    result = cursor.fetchall()
    for row in result:
        print(row)
