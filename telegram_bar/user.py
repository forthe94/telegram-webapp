from telegram_bar.transport import Transport


class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


class User:
    def __init__(self, x_pos: int, y_pos: int, transport: Transport, user_id: str) -> None:
        self.coordinates: Coordinate = Coordinate(x_pos, y_pos)
        self.connection: Transport = transport
        self.id: str = user_id