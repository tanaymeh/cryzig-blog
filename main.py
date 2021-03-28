from typing import Optional
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

import schemas, utils

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

@app.get('/')
async def home(req: Request, name: Optional[str]=None):
    if not name:
        name='User'
    return templates.TemplateResponse('index.html', 
                                      context={'request': req, 'name': name}
                                      )

@app.get('/users')
async def show_user(req: Request):
    """Displays all the users

    Args:
        req (Request): Generic request object
    """
    # Get all the users in a list using utility function
    allUsers = utils.Utils.getAllUsers('data/registry.json')
    if allUsers == -1:
        return templates.TemplateResponse('nousers.html',
                                   context={'request': req}
                                   )
    userNames = [x[1] for x in allUsers]
    return templates.TemplateResponse('users.html', 
                                      context={'request': req, 'all_users': userNames}
                                      )

@app.post('/createuser')
async def create_user(req: schemas.UserModel):
    # First check if the user exists in the registry
    userExists = utils.Utils.checkRegistry(req.userid)
    if userExists:
        return {'data': f'USER (id: {req.userid}, name: {req.name}) ALREADY EXISTS'}
    
    userFileName = utils.Utils.createUser(req)
    
    return {'data': f'Added User: {req.userid} to the registry with filename: {userFileName}'}