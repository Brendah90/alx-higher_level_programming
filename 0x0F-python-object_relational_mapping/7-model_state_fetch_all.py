#!/usr/bin/python3
"""Lists all State objects from the database"""
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
    all_states = session.query(State).order_by(State.id).all()
    for state in all_states:
        print(state.id, state.name, sep=": ")
