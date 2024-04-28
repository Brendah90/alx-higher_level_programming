#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user, password, db = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine, autoflush=False)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%'))

    for state in states:
        session.delete(state)
    session.commit()
