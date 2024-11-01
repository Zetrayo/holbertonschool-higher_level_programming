#!/usr/bin/python3
"""ye"""

import MySQLdb
import sys


def list_cities_by_state(username, password, database, state_name):
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
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # comment
    cities = [city[0] for city in cursor.fetchall()]
    print(", ".join(cities))

    # comment
    cursor.close()
    db.close()


if __name__ == "__main__":
    # comment
    list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
