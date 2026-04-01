import sys


class InputError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class InvalidInputError(Exception):
    def __init__(self):
        message = ("No scores provided. "
                   "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
                   )
        super().__init__(message)


def get_arguments(argv_list: list) -> None:
    for argument in sys.argv:
        argv_list.append(argument)


def convert_list_int(argv_list: list) -> list:
    int_list: list = []

    # add if statement for if not alphanumeric to raise InputError
    # raise "Invalid parameter: {argv_list[count]}")
    for count in range(len(argv_list)):
        int_list.append(int(argv_list[count]))


def count_total_score(list: list) -> int:
    total: int = 0

    for score in list:
        total += score

    return total


if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    argv_list: list = []
    count: int = 1
    list_size: int

    get_arguments(argv_list)
    list_size = len(argv_list)
    try:
        if list_size == 1:
            raise InvalidInputError()
        else:
            print(f"Total players: {list_size - 1}")
        for count in range(1, list_size):
            print(f"Argument {count}: {argv_list[count]}")
            count += 1
    except InputError as e:
        print(f"Invalid parameter: {e}")
    except InvalidInputError as e:
        print(f"{e}")
