from abc import ABC, abstractmethod
from typing import Any, cast, Protocol
# import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0
        self.stock_count: int = 0
        self._processed_count: int = 0

    def get_storage_size(self) -> int:
        return len(self._storage)

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def show_stats(self) -> tuple[int, int]:
        return (self._processed_count, self.stock_count)

    def output(self) -> tuple[int, str]:
        self.stock_count -= 1

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
                isinstance(x, (int, float, list)) and not isinstance(x, bool)
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
            self.stock_count += len(nodes)
            self._processed_count += len(nodes)
            self._storage.extend(nodes)
            self._rank += len(nodes)
        else:
            node: tuple[int, str] = (self._rank, str(data))
            self._storage.append(node)
            self._rank += 1
            self.stock_count += 1
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
            self.stock_count += len(nodes)
            self._processed_count += len(nodes)
            self._storage.extend(nodes)
            self._rank += len(nodes)
        else:
            node: tuple[int, str] = (self._rank, str(data))
            self._storage.append(node)
            self._processed_count += 1
            self.stock_count += 1
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
            self.stock_count += len(nodes)
            self._processed_count += len(nodes)
            self._storage.extend(nodes)
            self._rank += len(nodes)
        else:
            node: tuple[int, str] = (self._rank, str(data))
            self._storage.append(node)
            self._processed_count += 1
            self.stock_count += 1
            self._rank += 1


class ExportPlugin(Protocol):
    @abstractmethod
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSV_Export(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        result: str = ""
        i: int = 1
        for item in data:
            temp: str = item[1]
            if i == len(data):
                result += temp
            else:
                result += temp + ","
            i += 1
        print(f"{result}")


class JSON_Export(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        result: str = "{"
        i: int = 1
        for item in data:
            rank: str = str(item[0])
            value: str = item[1]
            if i == len(data):
                result += f"\"item_{rank}\": \"{value}\""
            else:
                result += f"\"item_{rank}\": \"{value}\", "
            i += 1
        result += "}"
        print(f"{result}")


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
        print("\n== DataStream statistics ==")
        if len(self.processors) <= 0:
            print("No processor found, no data")
        else:
            for processor in self.processors:
                stats: tuple[int, int] = processor.show_stats()
                print(f"{processor.__repr__()}: total {stats[0]}"
                      f" items processed, remaining {stats[1]} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        try:
            for processor in self.processors:
                exported_items: list[tuple[int, str]] = []
                for _ in range(nb):
                    if processor.get_storage_size() <= 0:
                        break
                    else:
                        exported_items.append(processor.output())
                plugin.process_output(exported_items)
        except Exception as e:
            print(f"{e}")


def test_m5_ex2() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("\nInitialize Data Stream...")

    Data_stream = DataStream()
    Data_stream.print_processors_stats()

    print("\nRegistering Processors")
    Num_processor = NumericProcessor()
    Text_processor = TextProcessor()
    Log_processor = LogProcessor()
    Data_stream.register_processor(Num_processor)
    Data_stream.register_processor(Text_processor)
    Data_stream.register_processor(Log_processor)

    stream: list[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42, ['Hi', 'five']]

    print(
        "\nSend first batch of data on stream: "
        "['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING', "
        "'log_message': 'Telnet access! Use ssh instead'}, "
        "{'log_level': 'INFO', 'log_message': 'User wil is connected'}],"
        " 42, ['Hi', 'five']]")

    Data_stream.process_stream(stream)
    Data_stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    CSV_export = CSV_Export()
    Data_stream.output_pipeline(3, CSV_export)
    Data_stream.print_processors_stats()

    print("\nSend another batch of data: [21, ['I love AI', "
          "'LLMs are wonderful', 'Stay healthy'], [{'log_level': 'ERROR',"
          " 'log_message': '500 server crash'}, {'log_level': 'NOTICE', "
          "'log_message': 'Certificate expires in 10 days'}], "
          "[32, 42, 64, 84, 128, 168], 'World hello']")

    stream = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
              [{'log_level': 'ERROR', 'log_message': '500 server crash'},
               {'log_level': 'NOTICE', 'log_message':
                   'Certificate expires in 10 days'}],
              [32, 42, 64, 84, 128, 168], 'World hello']

    Data_stream.process_stream(stream)
    Data_stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    JSON_export = JSON_Export()
    Data_stream.output_pipeline(5, JSON_export)
    Data_stream.print_processors_stats()


if __name__ == "__main__":
    test_m5_ex2()


"""
    print(f"{processor.__repr__()}: "
                      f"processor.get_storage_size(): "
                      f"{processor.get_storage_size()}"
                      f"\nexported_items: {exported_items}")
"""
