#!/usr/bin/python3
"""ye"""

import MySQLdb
import sys


def filter_states_by_name(username, password, database, state_name):
    """ye"""
    # comment
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # comment
    cursor = db.cursor()
    query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # comment
    states = cursor.fetchall()
    for state in states:
        print(state)

    # comment
    cursor.close()
    db.close()


if __name__ == "__main__":
    # comment
    filter_states_by_name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
