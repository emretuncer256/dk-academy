from dataclasses import dataclass
from typing import Literal


@dataclass
class User:
    name: str
    age: int
    gender: Literal["Erkek", "Kız"]
    interests: list[str] | None = None
