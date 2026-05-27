from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex2 import TransformCreatureFactory, HealingCreatureFactory
from ex2.battle_logic.battle_strategies import BattleStrategy
from ex2 import FlameFactory, AquaFactory
from ex2 import CreatureFactory
from typing import List, Tuple


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    i: int = 0
    for opponent in opponents:
        # opponent[0].
        opponents.pop(0)


def test_m7_ex2() -> None:

    Flame_fac: CreatureFactory = FlameFactory()
    Aqua_fac: CreatureFactory = AquaFactory()
    heal_fac: CreatureFactory = HealingCreatureFactory()
    Transf_fac: CreatureFactory = TransformCreatureFactory()
    
    bot_strat: NormalStrategy = NormalStrategy()
    def_strat: DefensiveStrategy = DefensiveStrategy()
    agro_strat: AggressiveStrategy = AggressiveStrategy()
    
    tournament_1 =[ (Flameling+Normal), (Healing+Defensive) ]
    print("Tournament 0 (basic)")



if __name__ == "__main__":
    test_m7_ex2()
