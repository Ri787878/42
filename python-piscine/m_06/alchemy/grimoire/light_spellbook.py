from .light_validator import validate_ingredients

def light_spell_allowed_ingredients() -> list[str]:
    return(["earth", "air", "fire", "water"])

def light_spell_record(spell_name: str, ingredients: str) -> str:
    result: str = "Spell recorded: " + spell_name + " (" + ingredients
    if validate_ingredients(ingredients) == "VALID":
        return result + " - VALID)"
    else:
        return result + " - INVALID)"
    