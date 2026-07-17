class Map_Selector():
    def print_maps(self) -> None:
        print("List of Available Maps:\n\tID:\tDificulty:\tName:")
        print("\t1\tEASY   \t\t01_linear_path")
        print("\t2\tEASY   \t\t02_simple_fork")
        print("\t3\tEASY   \t\t03_basic_capacity")
        print("\t4\tMEDIUM   \t01_dead_end_trap")
        print("\t5\tMEDIUM   \t02_circular_loop")
        print("\t6\tMEDIUM   \t03_priority_puzzle")
        print("\t7\tHARD   \t\t01_maze_nightmare")
        print("\t8\tHARD   \t\t02_capacity_hell")
        print("\t9\tHARD   \t\t03_ultimate_challenge")
        print("\t10\tCHALLENGER   \t01_the_impossible_dream")
        print("\n\t11\tCUSTOM (To add a custum map write its name"
              " and place it in the custum-test folder)")

    def input_filter_choice(self, map_id: str) -> bool:
        if not map_id.isnumeric():
            print("\n[ERROR] - Try Again, thats not a valid map!\n\n")
            return False
        elif 1 <= int(map_id) <= 11:
            return True
        return False

    @classmethod
    def map_id_to_path(self, map_id: int) -> str:
        map_name: str = ""

        if map_id == 1:
            return "test-files/easy/01_linear_path.txt"
        if map_id == 2:
            return "test-files/easy/02_simple_fork.txt"
        if map_id == 3:
            return "test-files/easy/03_basic_capacity.txt"
        if map_id == 4:
            return "test-files/medium/01_dead_end_trap.txt"
        if map_id == 5:
            return "test-files/medium/02_circular_loop.txt"
        if map_id == 6:
            return "test-files/medium/03_priority_puzzle.txt"
        if map_id == 7:
            return "test-files/hard/01_maze_nightmare.txt"
        if map_id == 8:
            return "test-files/hard/02_capacity_hell.txt"
        if map_id == 9:
            return "test-files/hard/03_ultimate_challenge.txt"
        if map_id == 10:
            return "test-files/challenger/01_the_impossible_dream.txt"
        if map_id == 11:
            map_name = input("Write custum map name: ")
            if not map_name.endswith(".txt"):
                map_name += ".txt"
        return map_name

    @classmethod
    def select_map(self) -> str:
        selector = Map_Selector()

        while True:
            selector.print_maps()
            map_id: str = input("\nSelect the map you want to test: ")
            if selector.input_filter_choice(map_id):
                return selector.map_id_to_path(int(map_id))

        return 0
