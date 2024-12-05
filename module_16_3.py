from fastapi import FastAPI, Path
from typing import Annotated
from fastapi import HTTPException
# uvicorn module_16_3:app --reload


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20,
                                     example='UrbanUser', description='Enter username')],
        age: Annotated[int, Path(ge=18, le=120, example=24, description=(
                'Enter age'))]) -> str:
    new_id = str(int(max(users, key=int)) + 1)
    users.update({new_id: f'Имя: {username}, Возраст: {age}'})
    return f'User {new_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str,
        username: Annotated[str, Path(min_length=5, max_length=20,
                                     example='UrbanUser', description='Enter username')],
        age: Annotated[int, Path(ge=18, le=120, example=24, description=(
                'Enter age'))]) -> str:
    for key in users.keys():
        if key == user_id:
            users.update({key: f'Имя: {username}, Возраст: {age}'})
            return f'The user {user_id} is updated'
    raise HTTPException(status_code=404, detail="Задача не найдена")

@app.delete('/user/{user_id}')
async def del_user(user_id: str) -> str:
    for key in users.keys():
        if key == user_id:
            users.pop(user_id)
            return f'User {user_id} has been deleted'
    raise HTTPException(status_code=404, detail="Задача не найдена")