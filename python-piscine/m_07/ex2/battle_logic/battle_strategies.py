from abc import ABC, abstractmethod
from typing import TypeGuard
from ex0.utils import Creature
from ex1.creature_fam_gen2.transform_family import Shiftling, Morphagon
from ex1.creature_fam_gen2.healing_family import Sproutling, Bloomelle


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        return creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, (Shiftling, Morphagon))
    
    # transform, attack, revert
    # only for transform family
    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            return creature.transform() + creature.attack() + creature.revert()
        else:
            return f"Invalid Creature '{creature.__class__}' for this aggressive strategy"


class DefensiveStrategy(BattleStrategy):
    # attack, heal
    # only for healer family
    def act(self, creature: Sproutling | Bloomelle) -> str:
        return creature.attack() + creature.heal()

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, (Sproutling, Bloomelle))
