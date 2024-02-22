from dataclasses import dataclass


# @dataclass
# class Channel:
#     type: str
#     followers: int


@dataclass
class Post:
    message: str
    timestamp: int
