from abc import ABC, abstractmethod
from typing import Any, cast


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0
        self._stock_count: int = 0
        self._processed_count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def show_stats(self) -> tuple[int, int]:
        return (self._processed_count, self._stock_count)

    def output(self) -> tuple[int, str]:
        self._stock_count -= 1

        return (self._storage.pop(0))


class NumericProcessor(DataProcessor):
    def __repr__(self) -> str:
        return "Numeric Processor"

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
            self._stock_count += len(nodes)
            self._processed_count += len(nodes)
            self._storage.extend(nodes)
            self._rank += len(nodes)
        else:
            node: tuple[int, str] = (self._rank, str(data))
            self._storage.append(node)
            self._rank += 1
            self._stock_count += 1
            self._processed_count += 1


class TextProcessor(DataProcessor):
    def __repr__(self) -> str:
        return "Text Processor"

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
            self._stock_count += len(nodes)
            self._processed_count += len(nodes)
            self._storage.extend(nodes)
            self._rank += len(nodes)
        else:
            node: tuple[int, str] = (self._rank, str(data))
            self._storage.append(node)
            self._processed_count += 1
            self._stock_count += 1
            self._rank += 1


class LogProcessor(DataProcessor):
    def __repr__(self) -> str:
        return "Log Processor"

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
            self._stock_count += len(nodes)
            self._processed_count += len(nodes)
            self._storage.extend(nodes)
            self._rank += len(nodes)
        else:
            node: tuple[int, str] = (self._rank, str(data))
            self._storage.append(node)
            self._processed_count += 1
            self._stock_count += 1
            self._rank += 1


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []
        self.items_done_count: list[int] = []
        self.items_remaining_count: list[int] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append((proc))
        self.items_remaining_count.append(int(0))
        self.items_done_count.append(int(0))
        pass

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            handled: bool = False
            for processor in self.processors:
                if processor.validate(item):
                    processor.ingest(item)
                    handled = True
                    break

            if not handled:
                print(f"DataStream error - "
                      f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.processors) <= 0:
            print("No processor found, no data")
        else:
            for processor in self.processors:
                stats: tuple[int, int] = processor.show_stats()
                print(f" {processor.__repr__()}: total {stats[0]}"
                      f" items processed, remaining {stats[1]} on processor")


def test_m5_ex1() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")

    Data_stream = DataStream()
    Data_stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    Num_processor = NumericProcessor()
    Data_stream.register_processor(Num_processor)

    stream: list[Any] = ['Hello world', [3.14, -1, 2.71],
                         [{'log_level': 'WARNING',
                           'log_message': 'Telnet access! Use ssh instead'},
                          {'log_level': 'INFO', 'log_message':
                              'User wil isconnected'}], 42, ['Hi', 'five']]

    print(
        "\nSend first batch of data on stream: "
        "['Hello world', [3.14, -1, 2.71], "
        "[{'log_level': 'WARNING', 'log_message'"
        ": 'Telnet access! Use ssh instead'}, "
        "{'log_level': 'INFO', 'log_message':"
        " 'User wil isconnected'}], 42, ['Hi', 'five']]")

    Data_stream.process_stream(stream)
    Data_stream.print_processors_stats()

    print("\nRegistering other data processors")
    Text_processor = TextProcessor()
    Log_processor = LogProcessor()

    Data_stream.register_processor(Text_processor)
    Data_stream.register_processor(Log_processor)

    print("Send the same batch again")
    Data_stream.process_stream(stream)
    Data_stream.print_processors_stats()

    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        Num_processor.output()

    for _ in range(2):
        Text_processor.output()

    for _ in range(1):
        Log_processor.output()

    Data_stream.print_processors_stats()


if __name__ == "__main__":
    test_m5_ex1()
