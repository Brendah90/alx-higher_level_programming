#!/usr/bin/python3
"""
Displays all values in the states table of the database where name matches
the argument in a way that's safe from SQL injections.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    user, password, db, state_name = sys.argv[1:5]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        password=password,
        db=db,
        charset="utf8",
    )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name=%s ORDER BY id"
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
