from dataclasses import dataclass
from time import time

# @dataclass
# class Channel:
#     type: str
#     followers: int


@dataclass
class Post:
    message: str
    timestamp: int

    def ready_to_post(self) -> bool:
        return self.timestamp <= time()
