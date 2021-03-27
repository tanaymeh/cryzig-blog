from fastapi import FastAPI
from typing import Optional, Union
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return "Home Page."