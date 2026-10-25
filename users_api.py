from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Users API",
    description="Учебное API: создание, изменение и удаление пользователей",
    version="1.0",
    swagger_ui_parameters={
        "syntaxHighlight": {"theme": "obsidian"},
        "deepLinking": True,
        "displayRequestDuration": True,
        "tryItOutEnabled": True,
        "defaultModelsExpandDepth": -1,
    },
)

class User(BaseModel):
    name: str
    age: int
    email: str

users = [
    {"id": 1, "name": "Tom", "age": 20, "email": "tom@mail.ru"},
    {"id": 2, "name": "Bob", "age": 22, "email": "bob@mail.ru"},
]
next_id = 3

def find_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

@app.get("/users", tags=["Пользователи"], summary="Список всех пользователей")
def get_users():
    return users

@app.get("/users/{user_id}", tags=["Пользователи"], summary="Получить одного пользователя")
def get_user(user_id: int):
    user = find_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user

@app.post("/users", tags=["Пользователи"], summary="Создать пользователя", status_code=201)
def create_user(data: User):
    global next_id
    new_user = {"id": next_id, "name": data.name, "age": data.age, "email": data.email}
    users.append(new_user)
    next_id = next_id + 1
    return new_user

@app.put("/users/{user_id}", tags=["Пользователи"], summary="Изменить пользователя")
def update_user(user_id: int, data: User):
    user = find_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    user["name"] = data.name
    user["age"] = data.age
    user["email"] = data.email
    return user

@app.delete("/users/{user_id}", tags=["Пользователи"], summary="Удалить пользователя")
def delete_user(user_id: int):
    user = find_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    users.remove(user)
    return {"message": "Пользователь удалён", "user": user}
