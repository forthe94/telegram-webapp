from fastapi import FastAPI
from fastapi.responses import FileResponse

file_path = "index.html"
app = FastAPI()

@app.get("/")
def main():
    return FileResponse(path=file_path, filename=file_path, media_type='text/html')
