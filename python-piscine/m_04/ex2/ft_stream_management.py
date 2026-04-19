import sys
import typing


def get_argv() -> list:
    argv_list: list = []
    for argument in sys.argv[1:]:
        argv_list.append(argument)

    return argv_list


def read_file(path: str) -> typing.Optional[str]:
    try:
        f = open(path, "r")
        text = f.read()
        f.close()
        return text
    except OSError as e:
        print(f"[STDERR] Error opening file '{path}': {e}")
        return None


def transform_content(file_content: str) -> str:
    lines: list[str] = file_content.splitlines()
    transformed_lines: list[str] = []

    for line in lines:
        transformed_lines.append(line + "#")

    transformed: str = "\n".join(transformed_lines)
    if file_content.endswith("\n"):
        transformed += "\n"

    return transformed


def test_m4_ex2() -> None:
    files_path: list = get_argv()

    if len(files_path) != 1:
        print("Usage: ft_ancient_text.py <file>\n")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{files_path[0]}'")

        original_content: str | None = read_file(files_path[0])
        if original_content is None:
            return

        print(f"---\n\n{original_content}\n---")
        print(f"File '{files_path[0]}' closed.\n")

        transformed_content: str = transform_content(original_content)
        print(f"Transform data:\n---\n\n{transformed_content}\n---")

        new_file_name: str = input("Enter new file name (or empty): ")
        if not new_file_name:
            # add a option to not save if not waanted by the user
            print("Not saving data.")
        else:
            try:
                print(f"Saving data to '{new_file_name}'")
                new_file = open(new_file_name, 'w+')
                new_file.write(transformed_content)
                new_file.close()
                print(f"Data saved in file '{new_file_name}'.")
            except OSError as e:
                print(
                    f"[STDERR] Error opening file '{new_file_name}': {e}"
                    f"\nData not saved.")


if __name__ == "__main__":
    test_m4_ex2()
