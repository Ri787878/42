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


def test_water_error():
    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_plant_error():
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_garden_error():
    print("Testing catching all garden errors...")
    try:
        raise GardenError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise GardenError("Not enough water in the tank!")
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
