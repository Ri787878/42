

def read_file(path: str) -> tuple[bool, str]:
    output: tuple[bool, str]
    try:
        with open(path, "r") as f:
            text = f.read()
        output = (True, text)
        return output
    except OSError as e:
        output = (False, f"{e}")
        return output


def write_file(file_name: str, content: str) -> tuple[bool, str]:
    try:
        with open(file_name, 'w+') as new_file:
            new_file.write(content)
        return (True, "Content successfully written to file")
    except OSError as e:
        return (False, f"{e}")


def secure_archive(f_nm: str, mode: str, cont: str = "") -> tuple[bool, str]:
    output: tuple[bool, str] = (False, "")

    if mode == "r":
        ok, data = read_file(f_nm)
        output = (ok, data)
    elif mode == "w":
        ok, data = write_file(f_nm, cont)
        output = (ok, data)
    return output


def test_m4_ex3() -> None:
    print("=== Cyber Archives Security ===")
    output: tuple[bool, str]
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    output = secure_archive("/not/existing/file", "r")
    print(output)
    # (False, "[Errno 2] No such file or directory: '/not/existing/file'")

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    output = secure_archive("/etc/master.passwd", "r")
    print(output)
    # (False, "[Errno 13] Permission denied: '/etc/master.passwd'")

    print("\nUsing 'secure_archive' to read from a regular file:")
    output = secure_archive("ancient_fragment.txt", "r")
    print(output)
    # (True, '[FRAGMENT]')

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    output = secure_archive("test1.txt", "w", output[1])
    print(output)
    # (True, 'Content successfully written to file')


if __name__ == "__main__":
    test_m4_ex3()
