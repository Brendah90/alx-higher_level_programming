#!/usr/bin/python3
"""Lists all City objects from the database"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user, password, db = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (
        session.query(City)
        .order_by(City.id)
        .all()
    )

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
