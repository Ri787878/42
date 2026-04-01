def input_temperature(temp_str: str) -> int:
    temp = int(temp_str, base=10)
    if temp < 0:
        raise Exception(
            f"Caught input_temperature error: "
            f"{temp}°C is too cold for plants (min 0°C)")

    if temp > 40:
        raise Exception(
            f"Caught input_temperature error: "
            f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def garden_operations(operation_number) -> None:
    try:
        if operation_number == 0:
            input_temperature("abc")
        elif operation_number == 1:
            15 / 0
        elif operation_number == 2:
            with open("/non/existent/file", mode='r') as file:
                file.read(42)
        elif operation_number == 3:
            name = "Maria"
            name + 42
        else:
            print("Operation completed successfully\n")
            return
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileExistsError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")


def test_error_types() -> None:
    error_tests = [0, 1, 2, 3, 4]

    for test in error_tests:
        print(f"Testing operation {test}...")
        garden_operations(test)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
