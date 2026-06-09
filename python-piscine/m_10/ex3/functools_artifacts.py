import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        return functools.reduce(operator.add, spells)
    if operation == "multiply":
        return functools.reduce(operator.mul, spells)
    if operation == "max":
        return functools.reduce(lambda a, b: a if a > b else b, spells)
    if operation == "min":
        return functools.reduce(
                                lambda spell_a, spell_b: spell_a
                                if spell_a < spell_b else spell_b,
                                spells,)
    raise ValueError(f"Can't handle operation: {operation}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": functools.partial(base_enchantment, 50, "fire"),
        "water": functools.partial(base_enchantment, 50, "water"),
        "ice": functools.partial(base_enchantment, 50, "ice")
    }


def enchant(power: int, element: str, target: str) -> str:
    return (f"{element.capitalize()} "
            f"enchantment on {target} with {power} power")


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register
    def _(spell: int) -> str:
        return (f"Damage spell: {spell} damage")

    @dispatcher.register
    def _(spell: str) -> str:
        return (f"Enchantment: {spell}")

    @dispatcher.register
    def _(spell: list) -> str:
        return (f"Multi-cast: {len(spell)} spells")

    return dispatcher


def test_spell_reducer() -> None:
    print("\n- - - Testing spell reducer - - -")
    print(f"Sum: {spell_reducer([20, 30, 50], 'add')}")
    print(f"Product: {spell_reducer([24, 10000], 'multiply')}")
    print(f"Max: {spell_reducer([39, 4, 2, 40, 22], 'max')}")


def test_parcial_enhancer() -> None:
    print("\n- - - Testing partial enchanter - - -")
    enchants = partial_enchanter(enchant)
    print(enchants["fire"]("Sword"))
    print(enchants["ice"]("Shield"))


def test_memorized_febonnacci() -> None:
    print("\n- - - Testing memorized febonnacci - - -")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")


def test_spell_dispatcher() -> None:
    print("\n- - - Testing spell dispatcher - - -")
    dispatched_spell = spell_dispatcher()
    print(dispatched_spell(42))
    print(dispatched_spell("fireball"))
    print(dispatched_spell(["heal", "shield", "buff"]))
    print(dispatched_spell(4.5))


def main() -> None:

    test_spell_reducer()
    test_parcial_enhancer()
    test_memorized_febonnacci()
    test_spell_dispatcher()


if __name__ == "__main__":
    main()
