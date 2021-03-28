from fastapi import FastAPI
from . import schemas, utils

app = FastAPI()

@app.get('/')
def home():
    return {'data': 'home'}

@app.post('/createuser')
def create_user(req: schemas.UserModel):
    