from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex2 import TransformCreatureFactory, HealingCreatureFactory
from ex2.battle_logic.battle_strategies import BattleStrategy
from ex2 import FlameFactory, AquaFactory
from ex2 import CreatureFactory
from typing import List, Tuple, Any


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    creatures: list[Any] = [f[0].create_base() for f in opponents]
    strats: list[Any] = [strat[1] for strat in opponents]
    i: int = 0
    for i in range(len(creatures) - 1):
        creature = creatures[i]
        strat1: BattleStrategy = strats[i]
        j: int = 1
        for j in range(1, len(creatures)):
            opponent = creatures[j]
            strat2: BattleStrategy = strats[j]
            if creature.__repr__() != opponent.__repr__():
                print("\n* Battle *")
                print(f"{creature.describe()} \n vs.\n{opponent.describe()}")
                print(" now fight!")
                print(strat1.act(creature))
                print(strat2.act(opponent))
            j += 1
        i += 1
        j = 0


def test_m7_ex2() -> None:

    Flame_fac: CreatureFactory = FlameFactory()
    Aqua_fac: CreatureFactory = AquaFactory()
    heal_fac: CreatureFactory = HealingCreatureFactory()
    Transf_fac: CreatureFactory = TransformCreatureFactory()

    bot_strat: NormalStrategy = NormalStrategy()
    def_strat: DefensiveStrategy = DefensiveStrategy()
    agro_strat: AggressiveStrategy = AggressiveStrategy()

    tournament: List[Tuple[CreatureFactory, BattleStrategy]]
    tournament = [(Flame_fac, bot_strat), (heal_fac, def_strat)]
    print("Tournament 0 (basic)\n[ (Flameling+Normal), (Healing+Defensive) ]")
    print(f"*** Tournament ***\n{len(tournament)} opponents involved")
    battle(tournament)

    try:
        tournament = [(Flame_fac, agro_strat), (heal_fac, def_strat)]
        print("\nTournament 1 (error)")
        print("[ (Flameling+Aggresive), (Healing+Defensive) ]")
        print(f"*** Tournament ***\n{len(tournament)} opponents involved")
        battle(tournament)
    except Exception as e:
        print(f"Battle error, aborting tournament: {e}")

    try:
        tournament = [(Aqua_fac, bot_strat),
                      (heal_fac, def_strat),
                      (Transf_fac, agro_strat)]
        print("\nTournament 2 (multiple)")
        print("[ (Aquabub+Normal), (Healing+Defensive), "
              "(Transform+Aggressive) ]")
        print(f"*** Tournament ***\n{len(tournament)} opponents involved")
        battle(tournament)
    except Exception as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    test_m7_ex2()
