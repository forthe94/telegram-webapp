from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

file_path = "index.html"
app = FastAPI()

@app.get("/")
def main():
    with open(file_path, 'r') as file:
        return HTMLResponse(content=file.read())

@app.get("/ws_chat")
def main():
    with open('ws_chat.html', 'r') as file:
        return HTMLResponse(content=file.read())


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")