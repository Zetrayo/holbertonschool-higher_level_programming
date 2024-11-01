#!/usr/bin/python3
"""ye"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_all_states(username, password, database):
    """ye"""
    # comment
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # comment
    Session = sessionmaker(bind=engine)
    session = Session()

    # comment
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    # comment
    session.close()


if __name__ == "__main__":
    # comment
    list_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
