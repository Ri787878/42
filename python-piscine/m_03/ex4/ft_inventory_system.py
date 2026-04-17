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


def parse_one_item(item: str, inventory: dict[str, int]) -> tuple[str, int]:
    item_name: str
    qty_text: str
    if ":" not in item:
        raise InputError(f"Error - invalid parameter '{item}'")

    item_name, qty_text = item.split(":", 1)

    if not item_name:
        raise InputError(f"Error - invalid parameter '{item_name}")

    if item_name in inventory:
        raise InputError(f"Redundant item '{item_name}' - discarding")

    try:
        qty: int = int(qty_text)
    except ValueError as e:
        raise InputError(f"Quantity error for '{item_name}': {e}")

    return item_name, qty


def parse_inventory(raw_inventory: list[str]) -> tuple[dict, list]:
    inventory: dict[str, int] = {}
    errors: list[str] = []

    for item in raw_inventory:
        try:
            item_name: str
            qty: int
            item_name, qty = parse_one_item(item, inventory)
        except InputError as e:
            errors.append(str(e))
            continue

        inventory[item_name] = qty

    return inventory, errors


def print_percentages(inventory: dict[str, int]) -> None:
    nbr_items: int = sum(inventory.values())

    for item_name, i in inventory.items():
        percentage: float = i * 100 / nbr_items
        print(f"Item {item_name} represents {round(percentage, 1)}%")


def test_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    raw_inventory: list = get_argv()
    inventory: dict = {}
    errors: list[str] = []

    inventory, errors = parse_inventory(raw_inventory)

    for error in errors:
        print(error)

    print(f"Got inventory: {inventory}")
    print(f"Item list: {inventory.keys()}")

    print(
        f"Total quantity of the {len(inventory)}"
        f" items: {sum(inventory.values())}")

    print_percentages(inventory)

    max_key: str
    max_value: int
    max_key, max_value = max(inventory.items(), key=lambda kv: kv[1])
    print(
        f"Item most abundant: {max_key}"
        f" with quantity {max_value}")

    min_key: str
    min_value: int
    min_key, min_value = min(inventory.items(), key=lambda kv: kv[1])
    print(
        f"Item most abundant: {min_key}"
        f" with quantity {min_value}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")

    if errors:
        sys.exit(1)


if __name__ == "__main__":
    test_inventory_system()
