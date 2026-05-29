from abc import ABC, abstractmethod
from typing import Any
from ex0.utils import Creature
from ex1.creature_fam_gen2.transform_family import Shiftling, Morphagon
from ex1.creature_fam_gen2.healing_family import Sproutling, Bloomelle


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Any) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Any) -> str:
        if self.is_valid(creature):
            return str(creature.attack())
        else:
            raise Exception((f"'{creature.__repr__()}' "
                             f"is not a valid Creature."))

    def is_valid(self, creature: Any) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, (Shiftling, Morphagon))

    # transform, attack, revert
    # only for transform family
    def act(self, creature: Any) -> str:
        if self.is_valid(creature):
            return str(creature.transform() + "\n" +
                       creature.attack() + "\n" + creature.revert())
        else:
            raise Exception(f"Invalid Creature '{creature.__repr__()}' "
                            f"for this aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    # attack, heal
    # only for healer family
    def act(self, creature: Any) -> str:
        if self.is_valid(creature):
            return str(creature.attack() + "\n" + creature.heal())
        else:
            raise Exception(f"Invalid Creature '{creature.__repr__()}' "
                            f"for this aggressive strategy")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, (Sproutling, Bloomelle))
