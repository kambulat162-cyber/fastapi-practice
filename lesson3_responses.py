from fastapi import FastAPI, Response
from fastapi.responses import PlainTextResponse, HTMLResponse, JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return Response(content="Привет! Это простой текст", media_type="text/plain")

@app.get("/text")
def get_text():
    return PlainTextResponse(content="Это PlainTextResponse")

@app.get("/html")
def get_html():
    return HTMLResponse(content="<h1>Заголовок</h1><p>Это HTMLResponse</p>")

@app.get("/json")
def get_json():
    return JSONResponse(content={"name": "Max", "course": 2})

@app.get("/text2", response_class=PlainTextResponse)
def get_text2():
    return "Текст через response_class"

@app.get("/html2", response_class=HTMLResponse)
def get_html2():
    return "<h2>HTML через response_class</h2>"
