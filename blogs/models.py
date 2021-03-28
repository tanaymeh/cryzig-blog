from sqlalchemy import Column, Integer, String
from . import db

class BlogModel(db.base):
    __tablename__ = 'blog'
    blogId = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)