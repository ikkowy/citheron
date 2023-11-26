from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Registry(Base):
    __tablename__ = "registry"
    id = Column(Integer, primary_key=True)
    key = Column(String(64), unique=True, nullable=False)
    value = Column(String(256))
    readonly = Column(Boolean, nullable=False)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    firstname = Column(String(64))
    lastname = Column(String(64))
    email = Column(String(254), unique=True)
    pwhash = Column(String(256))
    enabled = Column(Boolean, nullable=False)

class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
