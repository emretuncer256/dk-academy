from dataclasses import dataclass
from models.user import User
from models.base import BaseModel


@dataclass
class Prompt(BaseModel):
    user: User
    lesson: str | None = None
    topic: str | None = None

    def to_json(self):
        return {
            "user": self.user.to_json(),
            "lesson": self.lesson,
            "topic": self.topic
        }
