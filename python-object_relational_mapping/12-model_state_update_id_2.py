#!/usr/bin/python3
"""
script that changes the name of a State object
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]
        ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter_by(id=2).update({"name": "New Mexico"})
    session.commit()
