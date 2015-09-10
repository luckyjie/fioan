from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
DeclarativeBase = declarative_base()

def db_connect():
#    return create_engine('sqlite:///./sqlalchemy.db?charset=utf-8',echo = True)

    return create_engine('sqlite:///./sqlalchemy.db',echo = True)

def create_myblog_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class MyBlog(DeclarativeBase):
    __tablename__ = 'myblog'

    id = Column(Integer, primary_key = True)
    title = Column('title', String(800))
    time = Column('time', String(200))
    read = Column('read', String(200))
