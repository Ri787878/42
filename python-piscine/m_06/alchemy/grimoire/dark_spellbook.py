from .dark_validator import validate_ingredients

def dark_spell_allowed_ingredients() -> list[str]:
    return(["bats", "frogs", "arsenic", "eyeball"])

def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result: str = "Spell recorded: " + spell_name + " (" + ingredients
    if validate_ingredients(ingredients) == "VALID":
        return result + " - VALID)"
    else:
        return result + " - INVALID)"
    