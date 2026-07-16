class Map_Selector():
    def print_maps(self) -> None:
        print("List of Available Maps:")
        print("\t1.\tEASY - 01_linear_path")
        print("\t2.\tEASY - 02_simple_fork")
        print("\t3.\tEASY - 03_basic_capacity.txt")
        print("\t4.\tMEDIUM - 01_dead_end_trap.txt")
        print("\t5.\tMEDIUM - 02_circular_loop.tx")
        print("\t6.\tMEDIUM - 03_priority_puzzle.txt")
        print("\t7.\tHARD - 01_maze_nightmare.txt")
        print("\t8.\tHARD - 02_capacity_hell.txt")
        print("\t9.\tHARD - 03_ultimate_challenge.txt")
        print("\t10.\tCHALLENGER - 01_the_impossible_dream.txt")
        print("\t11.\tCUSTUM (To add a custum map write its name"
              " and place it in the custum-test folder)")

    def input_filter_choice(self, map_id: str) -> bool:
        if not map_id.isnumeric():
            print("\n[ERROR] - Try Again, thats not a valid map!\n\n")
            return False
        elif 1 <= int(map_id) <= 11:
            return True
        return False

    @classmethod
    def select_map(self) -> str:
        selector = Map_Selector()

        while True:
            selector.print_maps()
            map_id: str = input("\nSelect the map you want to test: ")
            if selector.input_filter_choice(map_id):
                return map_id


        return ""
