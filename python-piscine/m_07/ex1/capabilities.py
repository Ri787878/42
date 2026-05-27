from abc import abstractmethod, ABC


class TransformCapability(ABC):
    @abstractmethod
    def transform(self, attribute: str) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str) -> str:
        pass
