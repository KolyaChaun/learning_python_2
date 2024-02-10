# CRUD (Create Read Update Delete) operations


# Created my own exception class
class NotFoundNumber(Exception):
    pass


# Database representation
team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 31, "number": 12},
]


# Application source code
# The function shows the data in the database
def repr_players(players: list[dict]):
    for player in players:
        print(
            f"\t[Player {player['number']}]: {player['name']},{player['age']}"
        )


# With this function you can add a player using a unique number
def player_add(name: str, age: int, number: int) -> dict:
    for player in team:
        if player["number"] == number:
            raise NotFoundNumber
    player: dict = {
        "name": name,
        "age": age,
        "number": number,
    }
    team.append(player)

    return player


# Function for updating data by player number
def player_update(name: str, age: int, number: int) -> dict:
    for player in team:
        if player["number"] == number:
            player["name"] = name
            player["age"] = age
            return player
    raise NotFoundNumber


# Function to remove a player by number
def player_delete(number: int) -> None:
    for player in team:
        if player["number"] == number:
            team.remove(player)
            return
    raise NotFoundNumber


def main():
    operations = ("add", "del", "repr", "exit", "update")

    while True:
        operation = input("Please enter the operation: ")
        if operation not in operations:
            print(f"Operation: '{operation}' is not available\n")
            continue

        if operation == "exit":
            print("Bye")
            break
        elif operation == "repr":
            repr_players(team)
        elif operation == "add":
            user_data = input(
                "Enter new player information[name,age,number]: "
            )
            # Input: 'Clark,19,22'
            user_items: list[str] = user_data.split(",")
            # Result: ['Clark', '19', '22']
            name, age, number = user_items
            try:
                player_add(name=name, age=int(age), number=int(number))
            except ValueError:
                print("Age and number of player must be integers\n\n")
                continue
            except NotFoundNumber:
                print(
                    f"Player number {number} already exists, please enter another player number"
                )
                continue
        elif operation == "update":
            user_data = input(
                "Enter the information you want to update by player number: "
            )
            user_items: list[str] = user_data.split(",")
            name, age, number = user_items
            try:
                player_update(name=name, age=int(age), number=int(number))
            except ValueError:
                print("Age and number of player must be integers\n\n")
                continue
            except NotFoundNumber:
                print(f"Update failed! Player number {number} does not exist")
                continue
        elif operation == "del":
            user_data = input(
                "Enter the number of the player you want to remove: "
            )
            try:
                player_delete(number=int(user_data))
            except ValueError:
                print("Age and number of player must be integers\n\n")
                continue
            except NotFoundNumber:
                print(
                    f"Failed to remove player! Player number {user_data} does not exist"
                )
                continue
        else:
            raise NotImplementedError


if __name__ == "__main__":
    main()
