#!/usr/bin/python3
"""Lists all cities of that state, using the database"""
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
    query = """SELECT cities.name FROM cities INNER JOIN states ON
     states.id=cities.state_id WHERE states.name=%s ORDER BY cities.id"""
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()
    cities = [row[0] for row in results]
    print(*cities, sep=", ")
    cursor.close()
    db.close()
