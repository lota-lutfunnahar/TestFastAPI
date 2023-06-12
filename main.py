from typing import Union, Optional

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
def index():
    return {'data':{'name':'Mst Lutfunnahar Lota'}}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}
    

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}


@app.get('/blog')
def allBlog(limit=10, published : bool = True, sort: Optional[str] = None):
    # only get ten published blogs
    if published:
        return {'data':f'{limit}  publised blog list'}
    else:
        return {'data': 'All the blogs'}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create(request: Blog):
    return {'data': f'Blog is created with title as {request.title}'}

@app.get('/getPublishData')
def publishData():
    return {'data': 'view all published data for this profile'}