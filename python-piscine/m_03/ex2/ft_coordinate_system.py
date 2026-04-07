# import math


class InvalidInputError(Exception):
    def __init__(self):
        super().__init__("Invalid syntax")


class InvalidCoordinatesError(Exception):
    def __init__(self):
        super().__init__("Invalid values: x, y and z must be floats")


def get_player_pos():
    print("Get a first set of coordinates")
    raw_input = input("Enter new coordinates as floats in format 'x,y,z': ")
    values_input = [value.strip() for value in raw_input.split(",")]

    if len(values_input) != 3 or any(value == "" for value in values_input):
        raise InvalidInputError()

    try:
        coordinates = tuple(float(value) for value in values_input)
    except ValueError as exc:
        raise InvalidCoordinatesError() from exc

    return coordinates


def test_game_coordenates_system():
    print("=== Game Coordinate System ===")
    try:
        player_coordenates = get_player_pos()
        print(f"Got a first tuple: {player_coordenates}")
    except (InvalidInputError, InvalidCoordinatesError) as error:
        print(error)


if __name__ == "__main__":
    test_game_coordenates_system()

    """print coordenates
    print(f"Got a first tuple: "
          f"({player_coordenates[0]}, "
          f"{player_coordenates[1]}, "
          f"{player_coordenates[2]})")
    """
