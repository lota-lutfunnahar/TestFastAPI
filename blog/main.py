from fastapi import FastAPI
from . import schemas
from . import models

from .database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def create(request: schemas.Blog):
    return 'creating'
    

@app.get('/blogdata')
def getBlog():
    return 'blog data'