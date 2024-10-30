from dataclasses import dataclass
from models.base import BaseModel
from typing import Literal


@dataclass
class User(BaseModel):
    name: str
    age: int
    gender: Literal["Erkek", "Kız"]
    interests: list[str] | None = None

    def to_json(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "interests": self.interests
        }
