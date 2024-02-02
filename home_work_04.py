from typing import Generator


class Player:
    def __init__(self, first_name: str, last_name: str):
        self.first_name: str = first_name
        self.last_name: str = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


team: list[Player] = [
    Player("John", "Smith"),
    Player("Marry", "Smith"),
    Player("Jack", "Hill"),
    Player("Nick", "Doe"),
    Player("John", "Doe"),
    Player("Marry", "Doe"),
]


def dedup(collection) -> Generator[str, None, None]:
    unique_names: list[str] = []
    for player in collection:
        if player.first_name not in unique_names:
            unique_names.append(player.first_name)
            yield player


for player in dedup(team):
    print(player)
