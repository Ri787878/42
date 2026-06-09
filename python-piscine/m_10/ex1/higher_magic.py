from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def explosion(target: str, power: int) -> str:
    return f"Explosion knockbacks and damages {target} for {power} HP"


def enhance(target: str, power: int) -> str:
    return f"Enhance increases streght of {target} by {power} Power"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
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


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequencer(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequencer


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
        # long_spell = spell_sequence([explosion, heal, enhance])
        # sequence = long_spell("Arthur", 15)
        # for spell in sequence:
        #     print(spell)
    except Exception as e:
        print(e)