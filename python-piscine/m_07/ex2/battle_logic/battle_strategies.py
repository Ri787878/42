from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def act(self) -> None:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self) -> None:
        # just .attack()
        pass

    def is_valid(self) -> bool:
        return False


class AggressiveStrategy(BattleStrategy):
    # transform, attack, revert 
    # only for transform family
    def act(self) -> None:
        pass

    def is_valid(self) -> bool:
        return False


class DefensiveStrategy(BattleStrategy):
    # attack, heal
    # only for healer family
    def act(self) -> None:
        pass

    def is_valid(self) -> bool:
        return False
