from alchemy.elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    result: str = ""
    result += "Healing potion brewed with '" + create_earth()
    result += "' and '" + create_air() + "'"
    return result


def strength_potion():
    result: str = ""
    result += "Strength potion brewed with '" + create_fire()
    result += "' and '" + create_water() + "'"
    return result
