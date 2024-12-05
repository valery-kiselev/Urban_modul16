from fastapi import FastAPI
# uvicorn module_16_1:app --reload


app = FastAPI()

@app.get('/')
async def main_page() -> str:
    return 'Главная страница'

@app.get('/user/admin')
async def admin_page() -> str:
    return 'Вы вошли как администратор'

@app.get('/user')
async def read_name(username: str, age: int) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

@app.get('/user/{user_id}')
async def read_id(user_id: int) -> str:
    return f'Вы вошли как пользователь № {user_id}'


