import asyncio
import json

from telegram_bar.message import CoordinatesChangeMessage
from telegram_bar.user import User


class World:
    def __init__(self):
        self.users: dict[str, User] = dict()

    async def connected_user_loop(self):
        pass

    def add_user(self, user: User):
        self.users[user.id] = user

    def remove_user(self, user: User):
        self.users.pop(user.id)

    async def proccess_message(self, message: str, user: User):
        message_dict = json.loads(message)
        match message_dict['type']:
            case 'coordinates_change':
                parsed_message = CoordinatesChangeMessage.parse_obj(message_dict)

                if parsed_message.new_x is not None:
                    self.users[user.id].coordinates.x = parsed_message.new_x

                if parsed_message.new_y is not None:
                    self.users[user.id].coordinates.y = parsed_message.new_y
                return True

    async def world_loop(self):
        while True:
            print(self.users)
            for user in self.users.values():
                await user.connection.send_message(', '.join([str(user.coordinates) for user in self.users.values()]))
            await asyncio.sleep(1)

world = World()
