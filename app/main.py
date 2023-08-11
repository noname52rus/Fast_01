from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .library.helpers import *
from app.routers import unsplash


app = FastAPI()
app.include_router(unsplash.router)


templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name="static")


@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    data = openfile('home.md')
    return templates.TemplateResponse('page.html', {'request': request, 'data': data})


@app.get('/page/{page_num}', response_class=HTMLResponse)
async def page(request: Request, page_num: str):
    data = openfile(page_num + '.md')
    return templates.TemplateResponse('page.html', {'request': request, 'data': data})