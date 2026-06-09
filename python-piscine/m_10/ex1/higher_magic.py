from typing import Callable
"""
def spell_sequence(spells: list[Callable]) -> Callable
"""


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def explosion(target: str, power: int) -> str:
    return f"Explosion knockbacks and damages {target} for {power} HP"


def enhance(target: str, power: int) -> str:
    return f"Enhance increases streght of {target} by {power} Power"


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:

    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell2(target, power), spell1(target, power))
    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:

    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(
    condition: Callable[[str], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:

    def conditional(target: str, power: int) -> str:
        if condition(target):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def is_target_allowed(target: str) -> bool:

    if "enemy" in target.lower():
        return True
    if "teammate" in target.lower():
        return False
    if "pet" in target.lower():
        return False
    return True


if __name__ == "__main__":
    combo1 = spell_combiner(heal, explosion)

    try:
        print("\nTesting spell combiner...")
        combo1_res: tuple[str, str] = combo1('Arthur', 15)
        print(f"Combined spell result: {combo1_res[0]}, {combo1_res[1]}")
        print("\nTesting power amplifier...")

        mega_explosion = power_amplifier(explosion, 10)
        print(mega_explosion("Arthur", 3))
        # mega_explosion = conditional_caster(is_target_allowed, explosion)
        # print(mega_explosion("Orc(enemy)", 45))
    except Exception as e:
        print(e)