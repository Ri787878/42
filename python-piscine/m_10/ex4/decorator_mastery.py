from collections.abc import Callable
import functools
from time import perf_counter, sleep


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = perf_counter() - start
        print(f"Spell completed in {elapsed_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if "power" in kwargs:
                power = kwargs["power"]
            else:
                power = next((arg for arg in args
                              if isinstance(arg, int)), None)
            if power is None or power < min_power:
                return ("Insufficient power for this spell")
            return (func(*args, **kwargs))
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def retry(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for retry in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if retry < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"attempt {retry}/{max_attempts}")
            return (f"Spell casting failed after {max_attempts} attempts")
        return wrapper
    return retry


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return (all(char.isalpha() or char.isspace() for char in name))

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power")


@spell_timer
def fireball(target: str) -> str:
    sleep(0.333)
    return f"Fireball cast on {target}!"


@retry_spell(max_attempts=3)
def unstable_spell() -> str:
    raise RuntimeError("Spell failed")


@retry_spell(max_attempts=3)
def stable_spell() -> str:
    return ("Waaaaaaagh spelled !")


def explosion(target: str, power: int) -> str:
    return f"Explosion knockbacks and damages {target} for {power} HP"


def test_spell_timer() -> None:
    print(" - - - Testing spell timer - - -")
    result = fireball("Goblin")
    print(f"Result: {result}")


def test_retrying() -> None:
    print("\n - - - Testing retrying spell... - - -")
    print(unstable_spell())
    print(stable_spell())


def test_mageguild() -> None:
    print(" - - - Testing MageGuild... - - - ")
    print("- test validate mage name:")
    print(f"'Alex': {MageGuild.validate_mage_name('Alex')}")
    print(f"'X1': {MageGuild.validate_mage_name('X1')}")
    guild = MageGuild()
    print("\n- test cast_spell:")
    print(f"Casting a spell with power 15: "
          f"{guild.cast_spell('Lightning', 15)}")
    print(f"Casting a spell with power 5: {guild.cast_spell('Fireball', 5)}")


def main() -> None:
    test_spell_timer()
    test_retrying()
    test_mageguild()


if __name__ == "__main__":
    main()
