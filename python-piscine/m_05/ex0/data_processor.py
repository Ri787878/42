from abc import ABC
from abc import abstractmethod
from typing import Any
# import typing


class DataProcessor(ABC):
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
        return (1, "Error")


class NumericProcessor(DataProcessor):
    # ingests int float lists of both types including mixed
    # then convert it to strings and store it internally
    def ingest(self, data: int | float | list[int | float]) -> None:
        try:
            if isinstance(data, list):
                for item in data:
                    int(item)
                    float(item)
            else:
                int(data)
                float(data)
        except (TypeError, ValueError):
            raise Exception("Got exception: Improper numeric data")

        if isinstance(data, list):
            self.value_list: list[str]
            for value in data:
                self.value_list.append(str(value))
        else:
            self.value: str = str(data)


class TextProcessor(DataProcessor):
    def ingest(self, data: str | list[str]) -> None:
        try:
            if isinstance(data, list):
                for item in data:
                    str(item)
            else:
                str(data)
        except (TypeError, ValueError):
            raise Exception("Got exception: Improper text data")

            self.value: str = str(data)


class LogProcessor(DataProcessor):
    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        try:
            if isinstance(data, list):
                for item in data:
                    for key in item.keys():
                        str(key)
                    for value in item.values():
                        str(value)
            else:
                for key in data.keys():
                    str(key)
                for value in data.values():
                    str(value)
        except (TypeError, ValueError):
            raise Exception("Got exception: Improper text data")

        if isinstance(data, list):
            self.data_str: list[str] | str
            for value in data:
                self.data_str.append(str(value))
        else:
            self.data_str: str = str(data)
