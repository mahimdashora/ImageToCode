#Create schemas
import datetime as dt
import pydantic as _pydantic

class _UserBase(_pydantic.BaseModel):
    email:str
class _UserCreate(_pydantic.BaseModel):
    hashed_password:str
    class Config:
        orm_mode :True
class User(_UserBase):
    id:int
    class config:
        orm_mode= True

class _ImageBase(_pydantic.BaseModel):
    
    fname:str
    text:str
class ImageCreate(_ImageBase):   
    pass
class Images(_ImageBase):  
    id:int
    owner_id: int
    date_created:dt.datetime
    date_last_updated:dt.datetime
    class config:
        orm_mode= True
