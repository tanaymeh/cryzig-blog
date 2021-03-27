from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import schemas, models, db

app = FastAPI()

# Create the DB
models.Model.metadata.create_all(db.engine)

def get_db():
    db_ = db.sessionLocal()
    try:
        yield db_
    finally:
        db_.close()

# Routes
@app.post('/blog')
def create(req: schemas.BlogData, db: Session = Depends(get_db)):
    new_blog = models.Model(title=req.title, body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog