class Plant:
    class Stats():
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def get_grow_calls(self) -> int:
            return self._grow_calls

        def get_age_calls(self) -> int:
            return self._age_calls

        def get_show_calls(self) -> int:
            return self._show_calls

        def increase_grow_call(self) -> None:
            self._grow_calls += 1

        def increase_age_call(self) -> None:
            self._age_calls += 1

        def increase_show_call(self) -> None:
            self._show_calls += 1

        def display_extra_stats(self) -> None:
            pass

    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = height
        self._inicial_height = height
        self._days = days
        self._stats = self.Stats()

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._days} days old")
        self._stats.increase_show_call()

    def grow(self, growth: int) -> None:
        total_growth: float
        total_growth = growth
        self._height += total_growth
        self._height = round(self._height, 1)
        self._stats.increase_grow_call()

    def age(self, days: int) -> None:
        self._days += days
        self._stats.increase_age_call()

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm")
        else:
            print(f"{self._name}: height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._days = age
            print(f"Age updated: {age} days")
        else:
            print("Rose: Error, age can't be negative")
            print("Age update rejected")

    def get_name(self) -> str:
        return self._name

    def get_days(self) -> int:
        return self._days

    def get_height(self) -> float:
        return self._height

    def simulate_growth(self, days: int, growth: int) -> None:
        count = 1
        while count <= days:
            print(f"=== Day {count} ===")
            print(f"{self._name}: {self._height}cm, {self._days} days old")
            self.age(1)
            self.grow(growth)
            count += 1

    @staticmethod
    def valid_age(days: int) -> bool:
        if days > 365:
            print(f"Is {days} days more than a year? -> True")
            return True
        else:
            print(f"Is {days} days more than a year? -> False")
            return False

    @classmethod
    def create_anonymous(cls: type["Plant"], name: str) -> "Plant":
        instance: "Plant" = cls(name, 0, 0)
        return instance


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days)
        self._color = color
        self._bloom = False
        self.show()

    def bloom(self) -> None:
        if (self._bloom):
            return
        else:
            self._bloom = True

    def get_bloom(self) -> bool:
        return self._bloom

    def is_blomming(self) -> None:
        if (self._bloom):
            print(f" {self.get_name()} is blooming beautifully!")
        else:
            print(f" {self.get_name()} has not bloomed yet")

    def get_color(self) -> str:
        return self._color

    def show(self) -> None:
        super().show()
        print(f" Color: {self.get_color()}")
        self.is_blomming()


class Seed(Flower):
    def __init__(
            self, name: str, height: float, days: int, color: str,
            total_seeds: int):
        self._total_seeds = total_seeds
        super().__init__(name, height, days, color)

    def get_total_seeds(self) -> int:
        return self._total_seeds

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.get_total_seeds()}")

    def bloom(self) -> None:
        super().bloom()
        self.set_seeds(42)

    def set_seeds(self, seeds: int) -> None:
        if self.get_bloom():
            self._total_seeds = seeds
        else:
            return


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def get_shade_calls(self) -> int:
            return self._shade_calls

        def increase_shade_call(self) -> None:
            self._shade_calls += 1

        def display_extra_stats(self) -> None:
            print(f" {self._shade_calls} shade")

    def __init__(self, name: str, height: int, days: int, trunk_size: float):
        print("=== Tree")
        super().__init__(name, height, days)
        self._stats: Tree.Stats = self.Stats()
        self._trunk_diameter = trunk_size
        self._shade = 0
        self.show()

    def produce_shade(self) -> None:
        self._stats.increase_shade_call()
        print(
            f"Tree {self.get_name()} now produces "
            f"a shade of {self.get_height():.1f}cm long"
            f" and {self.get_trunk_diameter():.1f}cm wide.")

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def get_shade(self) -> float:
        return self._shade

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.get_trunk_diameter():.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, days: int, harvest_season: str):
        print("=== Vegetable")
        super().__init__(name, height, days)
        self._harvest_season = harvest_season
        self._nutritional_value = 0
        self.show()

    def grow(self, days: int) -> None:
        super().grow(days)

    def age(self, days: int) -> None:
        super().age(days)
        self.increase_nutricional_value(days)

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def get_nutricional_value(self) -> int:
        return self._nutritional_value

    def increase_nutricional_value(self, nutricional_value: int) -> None:
        self._nutritional_value += nutricional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.get_harvest_season()}")
        print(f" Nutritional value: {self.get_nutricional_value()}")


def show_stats(plant: Plant) -> None:
    print(
        f"Stats: {plant._stats.get_grow_calls()} grow,"
        f" {plant._stats.get_age_calls()} age,"
        f" {plant._stats.get_show_calls()} show")
    plant._stats.display_extra_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    # Statistics Part
    print("=== Check year-old")
    Plant.valid_age(30)
    Plant.valid_age(400)
    print()

    # Flower Part
    print("=== Flower")
    Rose = Flower("Rose", 15, 10, "red")
    print("[statistics for Rose]")
    show_stats(Rose)
    print("[asking the rose to grow and bloom]")
    Rose.bloom()
    Rose.grow(8)
    Rose.show()
    print("[statistics for Rose]")
    show_stats(Rose)
    print()

    # Tree Part
    Oak = Tree("Oak", 200, 365, 5.0)
    print("[statistics for Oak]")
    show_stats(Oak)
    print("[asking the oak to produce shade]")
    Oak.produce_shade()
    print("[statistics for Oak]")
    show_stats(Oak)
    print()

    print("=== Seed")
    Sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
    print("[make sunflower grow, age and bloom]")
    Sunflower.grow(30)
    Sunflower.age(20)
    Sunflower.bloom()
    Sunflower.show()
    print("[statistics for Sunflower]")
    show_stats(Sunflower)
    print()

    print("=== Anonymous")
    Anonymous = Plant.create_anonymous("Unknown plant")
    Anonymous.show()
    print("[statistics for Unknown plant]")
    show_stats(Anonymous)
