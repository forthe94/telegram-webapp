from fastapi import FastAPI
from fastapi.responses import HTMLResponse

file_path = "index.html"
app = FastAPI()

@app.get("/")
def main():
    with open(file_path, 'r') as file:
        return HTMLResponse(content=file.read())
