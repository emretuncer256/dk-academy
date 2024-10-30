from abc import ABC
from abc import abstractmethod


class BaseModel(ABC):

    @abstractmethod
    def to_json(self):
        ...
