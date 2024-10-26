from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    interests: list[str]
