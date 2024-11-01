#!/usr/bin/python3
"""ye"""

import MySQLdb
import sys


def list_all_cities(username, password, database):
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
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # comment
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    # comment
    cursor.close()
    db.close()


if __name__ == "__main__":
    # comment
    list_all_cities(sys.argv[1], sys.argv[2], sys.argv[3])
