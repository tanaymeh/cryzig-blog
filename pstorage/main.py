from fastapi import FastAPI
from . import schemas, utils

app = FastAPI()

@app.get('/')
def home():
    return {'data': 'Home Page'}

@app.post('/createuser')
def create_user(req: schemas.UserModel):
    # First check if the user exists in the registry
    userExists = utils.Utils.checkRegistry(req.userid)
    if userExists:
        return {'data': f'USER (id: {req.userid}, name: {req.name}) ALREADY EXISTS'}
    
    userFileName = utils.Utils.createUser(req)
    
    return {
            'data': 
            f'Added User: {req.userid} to the registry with filename: {userFileName}'
        }
