from fastapi import WebSocket


class Transport:
    async def receive_message(self) -> str:
        raise NotImplemented

    async def send_message(self, text: str) -> None:
        raise NotImplemented


class WebSocketTransport(Transport):
    def __init__(self, connection: WebSocket):
        self.connection = connection

    async def receive_message(self) -> str:
        return await self.connection.receive_text()

    async def send_message(self, text: str):
        await self.connection.send_text(text)


class TestTransport(Transport):
    async def receive_message(self):
        pass

    async def send_message(self, text: str):
        pass