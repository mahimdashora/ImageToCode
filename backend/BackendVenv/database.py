import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DATABASE_URL="sqlite:///.database.db"


engine=_sql.create_engine(DATABASE_URL,connect_args={"check_same_thread":False})
Session