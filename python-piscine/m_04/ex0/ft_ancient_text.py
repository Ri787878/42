import sys
# import typing


def get_argv() -> list:
    argv_list: list = []
    for argument in sys.argv[1:]:
        argv_list.append(argument)

    return argv_list


def test_m4_ex0() -> None:
    files_list: list = get_argv()

    if len(files_list) != 1:
        print("Usage: ft_ancient_text.py <file>\n")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{files_list[0]}'")
        #  func open() returns an object
        # exposing a file-oriented API (w/ methods)
        try:
            f = open(files_list[0], "r")
            print("---\n")
            print(f"{f.read()}---")
            f.close()
            print(f"File '{files_list[0]}' closed.")

        except OSError as e:
            print(f"Error opening file '{files_list[0]}': {e}")


if __name__ == "__main__":
    test_m4_ex0()
