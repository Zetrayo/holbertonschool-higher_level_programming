#!/usr/bin/python3
"""ye"""

import MySQLdb
import sys


def list_states(username, password, database):
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
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # comment
    states = cursor.fetchall()
    for state in states:
        print(state)

    # comment
    cursor.close()
    db.close()


if __name__ == "__main__":
    # comment
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
