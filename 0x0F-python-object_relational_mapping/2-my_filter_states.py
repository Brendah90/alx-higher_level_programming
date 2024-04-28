#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table of the
database where name matches the argument.
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
    query = """SELECT * FROM states WHERE name LIKE BINARY '{}'
     ORDER BY id""".format(state_name)
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
