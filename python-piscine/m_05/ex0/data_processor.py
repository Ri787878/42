from abc import ABC, abstractmethod
from typing import Any, cast


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return (self._storage.pop(0))


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            items = cast(list[Any], data)
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in items)
        return False

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
            node: tuple[int, str] = (self._rank, str(data))
            self._storage.append(node)
            self._rank += 1


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
            item_values += [f"{d['log_level']}: {d['log_message']}"
                            for d in items]
            nodes = [(self._rank + i, v) for i, v in enumerate(item_values)]
            self._storage.extend(nodes)
            self._rank += len(nodes)
        else:
            node: tuple[int, str] = (self._rank, str(data))
            self._storage.append(node)
            self._rank += 1


def test_m5_ex0() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    Number_processor = NumericProcessor()
    num_test_1: int = 42
    print(f" Trying to validate input '{num_test_1}': "
          f"{Number_processor.validate(num_test_1)}")

    num_test_2: str = "Hello"
    print(f" Trying to validate input '{num_test_2}': "
          f"{Number_processor.validate(num_test_2)}")

    test_3: int = "foo"
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        Number_processor.ingest(test_3)
    except Exception as e:
        print(f' {e}')

    test_list: list[int | float] = [1, 2, 3, 4, 5]
    try:
        print(" Processing data: [1, 2, 3, 4, 5]\n Extracting 3 values...")
        Number_processor.ingest(test_list)
        i: int = 0
        while i < 3:
            print(f" Numeric value {i}: {Number_processor.output()[1]}")
            i += 1
    except Exception as e:
        print(f' {e}')

    print("\nTesting Text Processor...")
    Text_processor = TextProcessor()
    text_test_1: int = 42
    print(f" Trying to validate input '{text_test_1}': "
          f"{Text_processor.validate(text_test_1)}")

    text_test_2: list[str] = ['Hello', 'Nexus', 'World']
    print(" Processing data: ['Hello', 'Nexus', 'World']\n"
          " Extracting 1 value...")
    try:
        Text_processor.ingest(text_test_2)
        print(f" Text value 0: {Text_processor.output()[1]}")
    except Exception as e:
        print(f' {e}')

    print("\nTesting Log Processor...")
    Log_processor = LogProcessor()

    log_test_1 = 'Hello'
    print(f" Trying to validate input 'Hello': "
          f"{Log_processor.validate(log_test_1)}")

    log_test_2: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    try:
        Log_processor.ingest(log_test_2)
    except Exception as e:
        print(f" {e}")
    print(" Processing data: "
          "[{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, "
          "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]"
          "\n Extracting 2 values...")
    for i in range(2):
        log_output1: tuple[int, str] = Log_processor.output()
        print(f" Log entry {i}: {log_output1[1]}")


if __name__ == "__main__":
    test_m5_ex0()
