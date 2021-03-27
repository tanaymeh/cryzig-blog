from fastapi import FastAPI

app = FastAPI()

@app.post('/blog')
def create():
    return "Creating..."