from pydantic import BaseModel

class BlogModel(BaseModel):
    authid: int
    blogTitle: str
    author: str
    content: str