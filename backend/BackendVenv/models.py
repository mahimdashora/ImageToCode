#User model and todo model
import datetime as dt
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import passlib.hash as _hash
import database as _database
class User(_database.Base):
    __tablename__="users"
    id=_sql.Column(_sql.Integer,primary_key=True,index=True)
    email=_sql.Column(_sql.String,unique=True,index=True)
    hashed_password=_sql.Column(_sql.String)
    def verify_password( self ,password):
       return _hash.bcrypt.verify(password,self.hashed_password)
class Images(_database.Base):
    __tablename__="users"
    id=_sql.Column(_sql.Integer,primary_key=True,index=True)
    owner_id=_sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    fname=_sql.Column(_sql.String,index=True) #name of image that is being uploaded
    text=_sql.Column(_sql.String,index=True) # the text which will be extracted from image
    date_created=_sql.Column(_sql.DateTime,default=dt.datetime.utcnow)
    date_last_updated=_sql.Column(_sql.DateTime,default=dt.datetime.utcnow)