from fastapi import FastAPI, Path
from typing import Annotated
# uvicorn module_16_2:app --reload


app = FastAPI()

@app.get('/')
async def get_main() -> dict:
    return {'message': 'Главная страница'}

@app.get('/user/admin')
async def get_admin() -> dict:
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{username}/{age}')
async def read_name(
        username: Annotated[str, Path(min_length=5, max_length=20,
                                      example='UrbanUser', description='Enter username')],
        age: Annotated[int, Path(ge=18, le=120, example=24, description=(
                'Enter age'))]) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}

@app.get('/user/{user_id}')
async def read_id(user_id: Annotated[int, Path(ge=1, le=100, example=1,
                                               description='The ID must be a positive integer')]) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}
