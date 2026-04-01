class GardenError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Plant:
    def __init__(self, name: str) -> None:
        self.name = name
        self.water_status = False


def is_capitalized(string: str) -> bool:
    return string == string.capitalize()


def water_plant(plant_name: Plant) -> None:
    if is_capitalized(plant_name.name):
        plant_name.water_status = True
        print(f"Watering {plant_name.name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name.name}'")


def test_watering_system() -> None:
    Tomato = Plant("Tomato")
    Lettuce = Plant("Lettuce")
    Carrots = Plant("Carrots")
    lettuce = Plant("lettuce")

    valid_garden = [Tomato, Lettuce, Carrots]
    invalid_garden = [Tomato, lettuce]

    print("Testing valid plants...")
    print("Opening watering system")

    try:
        for plant in valid_garden:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for plant in invalid_garden:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print(".. ending tests and returning to main")
        print("Closing watering system\n")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
