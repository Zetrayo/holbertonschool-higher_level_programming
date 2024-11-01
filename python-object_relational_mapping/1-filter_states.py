#!/usr/bin/python3
"""ye"""

import MySQLdb
import sys


def list_states_starting_with_n(username, password, database):
    """ye"""
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # comment
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # comment
    states = cursor.fetchall()
    for state in states:
        print(state)

    # comment
    cursor.close()
    db.close()


if __name__ == "__main__":
    # comment
    list_states_starting_with_n(sys.argv[1], sys.argv[2], sys.argv[3])
