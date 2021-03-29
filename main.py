from typing import Optional
from fastapi import FastAPI, Request, Form
from fastapi import templating
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import schemas, utils

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates/')

@app.get('/')
async def home(req: Request, name: Optional[str]=None):
    return templates.TemplateResponse('index.html', context={'request': req})

@app.get('/createblog')
async def create_blog(req: Request):
    return templates.TemplateResponse('newblog.html',
                                context={'request': req})

@app.post('/createblog')
async def create_blog(
        req: Request,
        authorName: str=Form(...),
        blogTitle: str=Form(...),
        blogContent: str=Form(...)
    ):
    print(authorName, blogTitle, blogContent)
    # return
    # First check if the blog exists in the registry
    blogExists = utils.Utils.checkRegistry(str(req.authid))
    if blogExists:
        return -1
    
    blogData = utils.Utils.createUser(req)
    
    # return {'data': f'Added Blog: {req.authid} to the registry with filename: {blogData}'}

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

@app.get('/delete')
async def delete_blog_front(req: Request):
    """Front End that will have a form to delete an existing blog

    Args:
        req (Request): Generic request object
    """
    pass