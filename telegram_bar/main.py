import asyncio

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

from telegram_bar.transport import WebSocketTransport
from telegram_bar.user import User
from telegram_bar.world import world

file_path = "index.html"
app = FastAPI()


@app.on_event('startup')
async def on_startup() -> None:
    asyncio.create_task(world.world_loop())

@app.get("/")
def main():
    with open(file_path, "r") as file:
        return HTMLResponse(content=file.read())


@app.get("/ws_chat")
def ws_chat():
    with open("ws_chat.html", "r") as file:
        return HTMLResponse(content=file.read())


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print('New ws connection')
    user = User(0, 0, WebSocketTransport(websocket), int(websocket.client.port))

    world.add_user(user)
    while True:
        message = await user.connection.receive_message()
        res = await world.proccess_message(message, user)
        await websocket.send_text(f"Message result: {res}")
