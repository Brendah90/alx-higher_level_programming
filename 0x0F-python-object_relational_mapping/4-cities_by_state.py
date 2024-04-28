#!/usr/bin/python3
"""Lists all cities from the database"""
import MySQLdb
import sys

if __name__ == "__main__":
    user, password, db = sys.argv[1:4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        password=password,
        db=db,
        charset="utf8",
    )
    cursor = db.cursor()
    query = """SELECT cities.id, cities.name, states.name FROM cities
     INNER JOIN states ON states.id=cities.state_id ORDER BY cities.id"""
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
