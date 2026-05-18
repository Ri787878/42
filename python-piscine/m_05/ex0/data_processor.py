from abc import ABC
from abc import abstractmethod
from typing import Any
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
        self._rank = self._rank - 1
        return (self._storage[self._rank + 1])


class NumericProcessor(DataProcessor):
    def validate(self, data: int | float | list[int | float]) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, list)) and not isinstance(x, bool)
                       for x in data)
        return False

    # ingests int float lists of both types including mixed
    # then convert it to strings and store it internally
    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper numeric data")

        if isinstance(data, list):
            self.value_list = [str(value) for value in data]
        else:
            self.value = str(data)


class TextProcessor(DataProcessor):
    """
    def validate(self, data: str | list[str]) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False
    """

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper text data")

        if isinstance(data, list):
            self.value_list = [str(item) for item in data]
        else:
            self.value = str(data)


"""
class LogProcessor(DataProcessor):
    def validate(self, data: dict[str, str] | list[dict[str, str]]) -> bool:
        if isinstance(data, dict):
            return all(isinstance(key, str) and isinstance(value, str) for key, value in data.items())
        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(isinstance(key, str) and isinstance(value, str) for key, value in item.items())
                for item in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper text data")

        if isinstance(data, list):
            self.data_str = [str(value) for value in data]
        else:
            self.data_str = str(data)
"""


if __name__ == "__main__":
    Number_Processor = NumericProcessor()

    test_1: Any = 42
    print(f"Trying to validate input '{test_1}': "
          f"{Number_Processor.validate(test_1)}")

    test_2: Any = "Hello"
    print(f"Trying to validate input '{test_2}': "
          f"{Number_Processor.validate(test_2)}")

    test_3: Any = "foo"
    print(f"Test invalid ingestion of string 'foo' without prior validation:")

    #exit_node: tuple[int, str] = Number_Processor.output()
    #print(f"Trying to validate input '{exit_node[0]}': {exit_node[0]}")
