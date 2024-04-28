#!/usr/bin/python3
"""Prints the first State object from the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

if __name__ == '__main__':
    user, password, db = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db))
    Base.metadata.create_all(engine)
    session = scoped_session(
        sessionmaker(
            bind=engine
        )
    )
    first_state = session.query(State).first()
    if not first_state:
        print('Nothing')
    else:
        print(first_state.id, first_state.name, sep=": ")
