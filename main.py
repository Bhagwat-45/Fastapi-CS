from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from httpx import request

app = FastAPI(
    title="FastAPI Blog"
)

templates = Jinja2Templates(
    directory="templates"
)

app.mount("/static",StaticFiles(directory="static"),name="static")


posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]


@app.get("/",include_in_schema=False,name="home")
@app.get("/posts",include_in_schema=False,name="posts")
def home(request: Request):
    return templates.TemplateResponse(request,"home.html",{"posts" : posts,"title" : "Home"})

@app.get("/api/posts")
def get_posts():
    return posts
# Automatically converted to JSON Array

@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    for i in posts:
        if i.get("id") == post_id:
            return i
        
    return {
        "Error" : "Post not found"
    }

