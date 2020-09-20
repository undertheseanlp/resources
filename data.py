import sqlalchemy


engine = sqlalchemy.create_engine('sqlite:///data/dictionary.sqlite')
connection = engine.connect()

metadata = sqlalchemy.MetaData()

words = sqlalchemy.Table('words', metadata, autoload=True, autoload_with=engine)

entities = sqlalchemy.Table('entities', metadata, autoload=True, autoload_with=engine)