#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects, contained in the
database
"""
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

    states_cities = (
        session.query(State)
        .order_by(State.id)
        .all()
    )

    for state in states_cities:
        print(state.id, state.name, sep=": ")
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
