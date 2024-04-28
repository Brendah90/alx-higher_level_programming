#!/usr/bin/python3
"""Lists all states with a name starting with N from the database"""
import MySQLdb
import sys

if __name__ == "__main__":
    user, password, db = sys.argv[1:4]
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        password=password,
        db=db,
        charset="utf8",
    )
    cursor = connection.cursor()
    cursor.execute(
        "\
                   SELECT * FROM states \
                   WHERE name LIKE BINARY 'N%' \
                   ORDER BY id"
    )
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    connection.close()
