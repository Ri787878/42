class GardenError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def check_water_level(water_level: int) -> None:
    if water_level < 5:
        raise WaterError("Not enough water in the tank!")


def check_plant_status(plant_name: str) -> None:
    if plant_name == "tomato":
        raise PlantError("The tomato plant is wilting!")


def test_water_error():
    water_level = 3
    try:
        print("Testing WaterError...")
        check_water_level(water_level)
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_plant_error():
    try:
        print("Testing PlantError...")
        plant_name = "tomato"
        check_plant_status(plant_name)
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_garden_error():
    print("Testing catching all garden errors...")
    try:
        plant_name = "tomato"
        check_plant_status(plant_name)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        water_level = 3
        check_water_level(water_level)
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_plant_error()
    print()
    test_water_error()
    print()
    test_garden_error()
    print("\nAll custom error types work correctly!")
