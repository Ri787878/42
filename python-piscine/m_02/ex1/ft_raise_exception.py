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


def test_temperature() -> None:
    test_cases = ["25", "abc", "100", "-50"]

    for test in test_cases:
        print(f"Input data is '{test}'")
        try:
            temp: int = input_temperature(test)
            print(f"Temperature is now {temp}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")
        except Exception as e:
            print(f"{e}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
