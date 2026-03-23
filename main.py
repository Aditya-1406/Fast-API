from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published:bool = True
    rating: Optional[int] = None
    
post = [
    {
    "title": "First Post",
    "content": "This is the first content",
    "id" : 1
    },
    {
    "title": "Second Post",
    "content": "This is the Second content",
    "id" : 2
    }
    ]

@app.get("/")
async def root():
    return {"message":"Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data":post}

@app.post("/posts")
async def create_posts(post : Post):
    print(post)
    print(post.dict())
    return {'message' : 'Post created'}

@app.post("/posts")
async def create_posts(post : Post):
    print(post)
    print(post.dict())
    return {'message' : 'Post created'}