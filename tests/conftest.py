import asyncio
import uuid

import pytest

from telegram_bar.transport import TestTransport
from telegram_bar.user import User
from telegram_bar.world import World


@pytest.fixture(scope="session", autouse=True)
def event_loop() -> asyncio.AbstractEventLoop:
    return asyncio.get_event_loop()


@pytest.fixture(scope="session", autouse=True)
def world() -> World:
    test_world = World()
    return test_world


@pytest.fixture
def add_user(world) -> User:
    user = User(0, 0, TestTransport(), uuid.uuid4().hex)
    world.add_user(user)
    yield user
