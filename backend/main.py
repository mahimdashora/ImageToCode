import fastapi 
import fastapi.security as _security

import sqlalchemy.orm as _orm
import services as _services,schemas as _schemas

app=fastapi.FastAPI()


@app.post("/api/users")
async def create_user(user:_schemas.UserCreate,db:_orm.Session=fastapi.Depends()):
    pass