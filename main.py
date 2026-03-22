from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data":"These are the posts"}

@app.post("/posts")
async def create_posts(payload: dict = Body(...)):
    print(payload)
    return {'message' : 'Post created'}