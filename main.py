from typing import Union, Optional

from fastapi import FastAPI
from blog import schemas

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
    return {'data':{'1','2','3','4','5'}}


@app.get('/blog')
def allBlog(limit=10, published : bool = True, sort: Optional[str] = None):
    # only get ten published blogs
    if published:
        return {'data':f'{limit}  publised blog list'}
    else:
        return {'data': 'All the blogs'}


@app.post('/blog')
def create(request: schemas.Blog):
    return {'data': f'Blog is created with title as {request.title}'}


@app.get('/getPublishData')
def publishData():
    return {'data': 'view all published data'}
    
@app.get('/getview')
def view():
    return 'dfgdg' 