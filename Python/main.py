from fastapi import FastAPI
from pydantic import BaseModel #module(class)

app = FastAPI()
#instance of FastAPI module

info = [{'id':1,'name':'Aniket'}]

@app.get('/get') #url data read karane
def getdata():
    return info

@app.post('/post')
def postdata(id:int,name):
    dict1 = {'id':id,'name':name}
    info.append(dict1)
    return info 



class User(BaseModel):#Model.py
    id : int
    name : str

# @app.put('/put')
# def update(id:int,user:User):
#     for i in info:
#         if i["id"]==id:
#             i = user
#     return info
    

    
#harshal code
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI()

class Post(BaseModel):
    tittle : str
    content : str
    #id : int
    published : bool = True
    ratting : Optional[int] = None

my_post = [{'tittle':'tittle of post 1','content':'content of post 1','id':1},{'tittle':'tittle of post 2','content':'content of post 2','id':2}]

def find(id):
    for p in my_post:
        if(p["id"]==id):
            return p

def find_index(id):
    for i,p in enumerate(my_post):
        if(p["id"]==id):
            return i

@app.get('/')
def read1():
    return {'message':'Hello World'}

@app.get('/posts')
def read2():
    return {'data' : my_post}

'''@app.post('/createposts')
def create_posts(post:dict = Body(...)):#accessing data from body
    print(post)
    return {'new_post':f"tittle {post['tittle']} content {post['content']}"}'''

@app.post('/posts')
def create(post : Post):
    post_dict = post.dict()
    print(post)
    print(post.dict())
    my_post.append(post.dict())
    return {"data":my_post}

@app.get("/get_post/{id}")
def get_post(id:int):
    post = find(id)
    return {"data":post}

@app.get("/latest_post")
def get_post():
    post = my_post[len(my_post)-1]
    return post

@app.delete("/deletepost/{id}")
def delete(id:int):
    index = find_index(id)
    my_post.pop(index)
    return {"message":"your post is deleted successfully"}    
        