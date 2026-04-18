import sys
import typing


def get_argv() -> list:
    argv_list: list = []
    for argument in sys.argv[1:]:
        argv_list.append(argument)

    return argv_list


def append_text_every_line(f: typing.IO[str], text_to_append: str) -> None:
    for line in f:
        f.write(text_to_append)


def test_m4_ex1() -> None:
    files_list: list = get_argv()

    if len(files_list) != 1:
        print("Usage: ft_ancient_text.py <file>\n")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
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

        try:
            temp_file = open(files_list[0], "r")
            print("Transform data:\n---\n")
            append_text_every_line(temp_file, "#")
            print(f"{f.read()}---")

            choice: str = input("Enter new file name (or empty): ")
            if not choice:
                # add a option to not save if not waanted by the user
                pass

            f.close()
            print(f"File '{files_list[0]}' closed.")
        except OSError as e:
            print(f"Error opening file '{files_list[0]}': {e}")


if __name__ == "__main__":
    test_m4_ex1()
