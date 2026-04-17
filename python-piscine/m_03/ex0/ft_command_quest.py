import sys


if __name__ == "__main__":
    print("=== Command Quest ===")

    count: int = 1
    list_size: int

    list_size = len(sys.argv)

    print(f"Program name: {sys.argv[0]}")
    if list_size == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {list_size - 1}")
    for count in range(1, list_size):
        print(f"Argument {count}: {sys.argv[count]}")
        count += 1
    print(f"Total arguments: {count}")
