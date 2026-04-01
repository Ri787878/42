import sys


def get_arguments(argv_list: list) -> None:
    for argument in sys.argv:
        argv_list.append(argument)


if __name__ == "__main__":
    print("=== Command Quest ===")

    argv_list: list = []
    count: int = 1
    list_size: int

    get_arguments(argv_list)
    list_size = len(argv_list)

    print(f"Program name: {argv_list[0]}")
    if list_size == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {list_size - 1}")
    for count in range(1, list_size):
        print(f"Argument {count}: {argv_list[count]}")
        count += 1
    print(f"Total arguments: {count}")
