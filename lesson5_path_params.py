from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/users/admin")
def admin():
    return {"message": "Привет, админ"}

@app.get("/users/{id}")
def get_user(id: int):
    return {"user_id": id}

@app.get("/people/{name}/{age}")
def get_person(name: str, age: int):
    return {"name": name, "age": age}

@app.get("/items/{name}-{count}")
def get_item(name: str, count: int):
    return {"item": name, "count": count}

@app.get("/students/{name}/{age}")
def get_student(name: str = Path(min_length=3, max_length=20),
                age: int = Path(ge=18, lt=111)):
    return {"name": name, "age": age}

@app.get("/phone/{phone}")
def get_phone(phone: str = Path(pattern=r"^\d{11}$")):
    return {"phone": phone}
