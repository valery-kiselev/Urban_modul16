from fastapi import FastAPI
# uvicorn module_16_1:app --reload


app = FastAPI()

@app.get('/')
async def main_page() -> dict:
    return {'message': 'Главная страница'}

@app.get('/user/admin')
async def admin_page() -> dict:
    return {'message': 'Вы вошли как администратор'}

@app.get('/user')
async def user_name(username: str, age: int) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}

@app.get('/user/{user_id}')
async def user_id(user_id: int) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


