import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///data/dictionary.sqlite')
Base = declarative_base()
connection = engine.connect()

metadata = sqlalchemy.MetaData()


class Word(Base):
    __tablename__ = 'words'

    word = Column('word', String, primary_key=True)

class Entity(Base):
    __tablename__ = 'entities'

    id = Column('id', Integer, primary_key=True)
    name = Column('word', String)
    tag = Column('tag', String)

Session = sessionmaker(bind=engine)
session = Session()

words = session.query(Word)
entities = session.query(Entity)

def test_entities():
    for entity in entities:
        print(entity.name)

test_entities()

# words = sqlalchemy.Table('words', metadata, autoload=True, autoload_with=engine)
#
# entities = sqlalchemy.Table('entities', metadata, autoload=True, autoload_with=engine)
