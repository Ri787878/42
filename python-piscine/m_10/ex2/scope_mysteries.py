from collections.abc import Callable


def mage_counter() -> Callable:
    x: int = 0

    def counter() -> int:
        nonlocal x
        x += 1
        return x
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total: int = initial_power

    def accumulate(extra_power: int) -> int:
        return total + extra_power
    return accumulate


def enchantment_factory(enchantment_type) -> Callable:
    def enchant_description(item_name) -> str:
        return (f"{enchantment_type} {item_name}")
    return enchant_description


def memory_vault() -> dict[str, Callable]:
    storage: dict = {}

    def store(key: str, value: object) -> None:
        storage[key] = value

    def recall(key: str) -> object:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def test_mage_counter() -> None:
    print("--- Test mage counter ---\nTest 1 counter: ", end="")
    count1 = mage_counter()
    for _ in range(10):
        print(count1(), end=" ")
    print("\nTest 2 counters simultaneausly: ", end="")
    for _ in range(10):
        count2 = mage_counter()
        print(count2(), end=" ")
    print("\n")


def test_spell_accumulator() -> None:
    print("--- Test spell accumulator ---")
    power_ball = spell_accumulator(0)
    print(f"Start with 0: {power_ball(0)}")
    print(f"Then add 15: {power_ball(15)}")
    print(f"Then add 50: {power_ball(50)}\n")


def test_factory() -> None:
    print("--- Test enchantment factory ---")
    fac = enchantment_factory("Flaming")
    print("The enhancement is 'Flaming'\n")
    print("First item is: ", end="")
    print(fac("Sword"))
    print("Second item is: ", end="")
    print(fac("Spear"))
    print("Third item is: ", end="")
    print(fac("Shield"))
    print()


def test_vault() -> None:
    print("--- Test Memory Vault ---\n")
    vault = memory_vault()

    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    try:
        test_mage_counter()
        test_spell_accumulator()
        test_factory()
        test_vault()
        pass
    except Exception as e:
        print(e)
