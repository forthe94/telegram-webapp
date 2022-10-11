from pydantic import BaseModel


class BaseMessage(BaseModel):
    type: str


class CoordinatesChangeMessage(BaseMessage):
    new_x: int | None
    new_y: int | None
