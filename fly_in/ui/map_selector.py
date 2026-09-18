from variables import Files_in_use
from pathlib import Path


class Map_Selector():
    def print_maps(self) -> None:
        """Method lists list of preset available maps to use."""
        print("List of Available Maps:\n\tID:\tDifficulty:\tName:")

        for map_id, map_path in enumerate(self.preset_maps(), start=1):
            path = Path(map_path.value)
            difficulty = path.parent.name.upper()
            name = path.stem

            print(f"\t{map_id}\t{difficulty:<10}\t{name}")

        print(
            "\n\t11\tCUSTOM      "
            "\tWrite a custom map name"
        )

    @staticmethod
    def preset_maps() -> list[Files_in_use]:
        return [
            Files_in_use.LINEAR_PATH,
            Files_in_use.SIMPLE_FORK,
            Files_in_use.BASIC_CAPACITY,
            Files_in_use.DEAD_END_TRAP,
            Files_in_use.CIRCULAR_LOOP,
            Files_in_use.PRIORITY_PUZZLE,
            Files_in_use.MAZE_NIGHTMARE,
            Files_in_use.CAPACITY_HELL,
            Files_in_use.ULTIMATE_CHALLENGE,
            Files_in_use.THE_IMPOSSIBLE_DREAM,
        ]

    def input_filter_choice(self, map_id: str) -> bool:
        """Method to validate inputted map choice."""
        if not map_id.isnumeric():
            print("\n[ERROR] - Try Again, thats not a valid map!\n\n")
            return False
        elif 1 <= int(map_id) <= 11:
            return True
        return False

    @classmethod
    def map_id_to_path(cls, map_id: int) -> str:
        maps = cls.preset_maps()

        if 1 <= map_id <= len(maps):
            return maps[map_id - 1].value

        if map_id == 11:
            map_name = input("Write custom map name: ")
            if not map_name.endswith(".txt"):
                map_name += ".txt"
            return map_name

        return ""

    @classmethod
    def select_map(self) -> str:
        """Method to chose which map to use."""
        selector = Map_Selector()

        while True:
            selector.print_maps()
            map_id: str = input("\nSelect the map you want to test: ")
            if selector.input_filter_choice(map_id):
                return selector.map_id_to_path(int(map_id))

        return 0
