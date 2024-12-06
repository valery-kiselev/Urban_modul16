from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
# uvicorn module_16_4:app --reload


app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    age: int

users = []

@app.get('/users')
async def get_user() -> List[User]:
    return users

@app.post('/user/{username}/{age}', response_model=User)
async def create_user(user: User) -> str:
    new_id = max((u.id for u in users), default=0) + 1
    new_user = User(id=new_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user

@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(user_id: int, user: User):
    for u in users:
        if u.id == user_id:
            u.username = user.username
            u.age = user.age
            return u
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete('/user/{user_id}', response_model=str)
async def delete_user(user_id: int):
    for u in users:
        if u.id == user_id:
            users.remove(u)
            return f"Пользователь с ID {user_id} удален."
    raise HTTPException(status_code=404, detail="User was not found")
