#!/usr/bin/python3
"""
Contains the class definition of a State and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    """State class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
