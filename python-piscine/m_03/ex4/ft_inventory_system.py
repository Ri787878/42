import sys


class InputError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


def get_argv() -> list:
    argv_list: list = []
    for argument in sys.argv[1:]:
        argv_list.append(argument)

    return argv_list

# Diferent errors possible:
#   Repeated Item
#   Invalid parameter(has no amount ":amount")
#   Quantity error - no int is passed


def parse_inventory(raw_inventory: list[str]) -> dict:
    inventory: dict[str, int] = {}
    errors: list[str] = []

    for item in raw_inventory:
        try:
            item_name: str
            qty_text: str
            item_name, qty_text = item.split(":", 1)

            if item_name in inventory:
                raise InputError(f"Redundant item '{item_name}' - discarding")

        except ValueError:
            raise InputError(f"Error - invalid parameter '{item}'")
        except InputError as e:
            errors.append(str(e))

        try:
            qty = int(qty_text)
        except ValueError as e:
            raise InputError(f"Quantity error for '{item_name}': {e}")

        inventory[item_name] = qty

    return inventory


def test_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    raw_inventory: list = get_argv()

    try:
        inventory = parse_inventory(raw_inventory)
        print(inventory)
    except InputError as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    test_inventory_system()




"""
    coordenates: list = []
    for value in values_input:
        try:
            coordenates.append(float(value))
        except ValueError:
            raise InputError(
                f"Error on parameter '{value}': "
                f"could not convert string to float: '{value}'")
    return tuple(coordenates)
"""
