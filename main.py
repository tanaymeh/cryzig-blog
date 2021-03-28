from typing import Optional
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import schemas, utils

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates/')

@app.post('/createblog')
async def create_blog(req: schemas.BlogModel):
    # First check if the blog exists in the registry
    userExists = utils.Utils.checkRegistry(req.userid)
    if userExists:
        return {'data': f'USER (id: {req.authid}, name: {req.author}) ALREADY EXISTS'}
    
    userFileName = utils.Utils.createUser(req)
    
    return {'data': f'Added User: {req.authid} to the registry with filename: {userFileName}'}

@app.get('/')
async def home(req: Request, name: Optional[str]=None):
    return templates.TemplateResponse('index.html', context={'request': req})

@app.get('/blogs')
async def show_blogs(req: Request):
    """Displays all the blogs

    Args:
        req (Request): Generic request object
    """
    # Get all the users in a list using utility function
    allBlogs = utils.Utils.getAllBlogs('data/registry.json')
    if allBlogs == -1:
        return templates.TemplateResponse('noblogs.html',
                                   context={'request': req}
                                   )
    blogTitles = [x[1] for x in allBlogs]
    return templates.TemplateResponse('blogs.html', 
                                      context={'request': req, 'all_users': blogTitles}
                                    )

@app.get('/newblog')
async def new_blog_front(req: Request):
    """Front End that will have a form to create a new blog

    Args:
        req (Request): Generic request object
    """
    pass

@app.get('/delete')
async def delete_blog_front(req: Request):
    """Front End that will have a form to delete an existing blog

    Args:
        req (Request): Generic request object
    """
    pass