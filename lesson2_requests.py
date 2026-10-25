from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Главная страница"}

@app.get("/about")
def about():
    return {"message": "О сайте"}

@app.get("/contacts")
def contacts():
    return {"email": "student@example.com", "phone": "88005553535"}

@app.get("/numbers")
def numbers():
    return [1, 2, 3, 4, 5]
