from pydantic import BaseModel
from typing import Union, Optional

class BlogData(BaseModel):
    """
    Schema for Blog data consumed on a post request to /blog
    """
    title: str
    content: str
    serialNum: int
    date: Optional[str]