#to create database
import database as _database
def create_database():#This function will create database.db file
    return _database.Base.metadata.create_all(bind=_database.engine)
def get_db():
    db=