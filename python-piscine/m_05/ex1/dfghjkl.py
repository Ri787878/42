from abc import ABC, abstractmethod
from typing import Any, cast
# import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0

    # check whether the input data is right for the current data processor
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    # process the input data
    # needs to raise a Exception if user doesnt validate the data before hand
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        self._rank -= 1
        return (self._storage.pop(0))


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            items = cast(list[Any], data)
            return all(isinstance(x, (int, list)) and not isinstance(x, bool)
                       for x in items)
        return False

    # ingests int float lists of both types including mixed
    # then convert it to strings and store it internally
    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper numeric data")

        if isinstance(data, list):
            items = cast(list[Any], data)
            nodes = [(self._rank + i, str(v)) for i, v in enumerate(items)]
            self._storage.extend(nodes)
            self._rank += len(nodes)
        else:
            node: tuple[int, str] = (self._rank, str(data))
            self._storage.append(node)
            self._rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            items = cast(list[Any], data)
            return all(isinstance(item, str) for item in items)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper text data")

        if isinstance(data, list):
            items = cast(list[Any], data)
            nodes = [(self._rank + i, v) for i, v in enumerate(items)]
            self._storage.extend(nodes)
            self._rank += len(nodes)
        else:
            self.value = str(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            values_dict = cast(dict[Any, Any], data)
            return all(isinstance(key, str)
                       and isinstance(value, str)
                       for key, value in values_dict.items())
        if isinstance(data, list):
            values = cast(list[Any], data)
            return all(
                isinstance(item, dict)
                and all(isinstance(key, str)
                        and isinstance(value, str)
                        for key, value in cast(dict[Any, Any], item).items())
                for item in values
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper text data")

        if isinstance(data, list):
            items = cast(list[Any], data)
            item_values: list[str] = []
            item_values += [v for d in items for v in d.values()]
            nodes = [(self._rank + i, v) for i, v in enumerate(item_values)]
            self._storage.extend(nodes)
            self._rank += len(nodes)
        else:
            self.value = str(data)


def test_m5_ex1() -> None:
    print("=== Code Nexus - Data Stream ===")

    print("\nInitialize Data Stream...")
    print("\n== DataStream statistics ==")
    # ADD TEST FOR FOUNDING PROCESSORES, AND DATA

    print("\nRegistering Numeric Processor")
    # Number_processor = NumericProcessor()

    print("\n")
    # Text_processor = TextProcessor()

    print("\nTesting Log Processor...")
    # Log_processor = LogProcessor()


if __name__ == "__main__":
    test_m5_ex1()
