from ..elements import create_air
from ..potions import strength_potion
import alchemy


def lead_to_gold() -> str:
    res: str = ""
    res += "Recipe transmuting Lead to Gold: brew'" + create_air() + "'"
    res += "and '" + strength_potion() + "'"
    res += " mixed with '" + alchemy.create_air() + "'"
    return res


print(lead_to_gold())
