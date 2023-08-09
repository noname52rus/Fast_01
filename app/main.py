from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name="static")


@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    data = {
        'page' : 'Home Page'
    }
    return templates.TemplateResponse('page.html', {'request': request, 'data': data})


@app.get('/page/{page_num}', response_class=HTMLResponse)
async def page(request: Request, page_num: str):
    data = {
        'page' : page_num
    }
    return templates.TemplateResponse('page.html', {'request': request, 'data': data})