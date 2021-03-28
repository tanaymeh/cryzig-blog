from pydantic import BaseModel

class UserModel(BaseModel):
    userid: str
    name: str
    age: int
    gender: str