from abc import ABC, abstractmethod
import typing


class Creature(ABC):
    def __init__(self, name: str, type: str):
        self._name = name
        self._type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    @abstractmethod
    def describe(self) -> str:
        pass
