from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated, List
# uvicorn module_16_5:app --reload


app = FastAPI(swagger_ui_parameters={'tryItOutEnabled': True}, debug=True)
templates = Jinja2Templates(directory='templates')

class User(BaseModel):
    id: int
    username: str
    age: int

users = []

@app.get('/', response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})

@app.get('/user/{user_id}', response_class=HTMLResponse)
async def get_user(request: Request, user_id: Annotated[int, Path(ge=1)]):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id - 1]})
    raise HTTPException(status_code=404, detail='User not found')

@app.post('/users/{username}/{age}', response_class=HTMLResponse)
async def create_user(request: Request, username: Annotated[str, Path(min_length=3, max_length=20)], age: Annotated[int, Path(ge=18, le=100)]):
    new_id = max([user.id for user in users]) + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})

@app.put('/users/{user_id}/{username}/{age}', response_class=HTMLResponse)
async def update_user(request: Request, user_id: Annotated[int, Path(ge=1)], username: Annotated[str, Path(min_length=3, max_length=20)], age: Annotated[int, Path(ge=18, le=100)]):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return templates.TemplateResponse('users.html', {'request': request, 'users': users})
    raise HTTPException(status_code=404, detail='User not found')

@app.delete('/users/{user_id}', response_class=HTMLResponse)
async def delete_user(request: Request, user_id: Annotated[int, Path(ge=1)]):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return templates.TemplateResponse('users.html', {'request': request, 'users': users})
    raise HTTPException(status_code=404, detail='User not found')