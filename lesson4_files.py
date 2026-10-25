from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("public/index.html")

@app.get("/file", response_class=FileResponse)
def get_file():
    return "public/index.html"

@app.get("/download")
def download():
    return FileResponse("public/index.html",
                        filename="mainpage.html",
                        media_type="application/octet-stream")
