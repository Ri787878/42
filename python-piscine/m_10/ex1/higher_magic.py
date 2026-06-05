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


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int):
        return (spell2(target, power), spell1(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> Callable:
        return(base_spell(target, power * multiplier))
    return amplifier


def conditional_caster(condition: Callable[[str, int], bool], spell: Callable[[str, int], str]) -> Callable[[str, int], str]:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional

if __name__ == "__main__":
    combo1 = spell_combiner(heal, explosion)

    try:
        print("Testing spell combiner...")
        combo1_res: tuple[str, str] = combo1('Arthur', 15)
        print(f"Combined spell result: {combo1_res[0]}, {combo1_res[1]}")
        # print("Testing power amplifier...")

        mega_explosion = power_amplifier(explosion, 10)
        print(mega_explosion("Arthur", 45))
        mega_explosion = conditional_caster(explosion)
        print(mega_explosion("Arthur", 45))
    except Exception as e:
        print(e)