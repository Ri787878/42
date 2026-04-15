import math


class InvalidInputError(Exception):
    def __init__(self) -> None:
        super().__init__("Invalid syntax")


class InvalidCoordinatesError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


def parse_coordenates(raw_input: str) -> tuple:
    values_input = [value.strip() for value in raw_input.split(",")]
    if len(values_input) != 3 or any(value == "" for value in values_input):
        raise InvalidInputError()

    coordenates: list = []
    for value in values_input:
        try:
            coordenates.append(float(value))
        except ValueError:
            raise InvalidCoordinatesError(
                f"Error on parameter '{value}': "
                f"could not convert string to float: '{value}'")
    return tuple(coordenates)


def get_player_pos() -> tuple:
    while True:
        raw_input: str = input(
            "Enter new coordinates as floats in format 'x,y,z': ")

        try:
            return parse_coordenates(raw_input)
        except InvalidInputError as e:
            print(e)
        except InvalidCoordinatesError as e:
            print(e)


def calculate_3d_distance(point1: tuple, point2: tuple) -> float:
    temp: float = 0.0
    for i in range(3):
        temp += (point1[i] - point2[i]) ** 2
    return round(math.sqrt(temp), 4)


def test_game_coordenates_system() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")

    player1_coords: tuple = get_player_pos()
    print(f"Got a first tuple: {player1_coords}")
    print(
        f"It includes: X={player1_coords[0]}, "
        f"Y={player1_coords[1]}, "
        f"Z={player1_coords[2]}")

    center: tuple = (0, 0, 0)
    distance_to_center: float = calculate_3d_distance(center, player1_coords)
    print(f"Distance to center: {distance_to_center}")

    print("\nGet a second set of coordinates")
    player2_coords: tuple = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: "
          f"{calculate_3d_distance(player1_coords, player2_coords)}")


if __name__ == "__main__":
    test_game_coordenates_system()
