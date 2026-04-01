class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = height
        self._days = days
        print(f"{self._name}: {self._height:.1f}cm, {self._days} days old")

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._days} days old")

    def grow(self, days: int) -> None:
        total_growth: float
        total_growth = 2.1 * days
        self._height += total_growth
        self.age(days)
        self._height = round(self._height, 1)

    def age(self, days: int) -> None:
        self._days += days

    def set_height(self, height: float):
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm")
        else:
            print(f"{self._name}: height can't be negative")
            print("Height update rejected")

    def set_age(self, age):
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
            self.age()
            self.grow(growth)
            count += 1


class Flower(Plant):
    def __init__(self, name, height, days, color):
        print("=== Flower")
        super().__init__(name, height, days)
        self._color = color
        self._bloom = False
        print(f" Color: {self.get_color()}")
        self.is_blomming()

    def bloom(self) -> None:
        if (self._bloom):
            return
        else:
            self._bloom = True

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


class Tree(Plant):
    def __init__(self, name, height, days, trunk_size):
        print("=== Tree")
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_size
        print(f" Trunk diameter: {self.get_trunk_diameter():.1f}cm")

    def produce_shade(self):
        print(
            f"Tree {self.get_name()} now produces "
            + f"a shade of {self.get_height():.1f}cm long"
            + f" and {self.get_trunk_diameter():.1f}cm wide.")

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.get_trunk_diameter():.1f}cm")


class Vegetable(Plant):
    def __init__(self, name, height, days, harvest_season):
        print("=== Vegetable")
        super().__init__(name, height, days)
        self._harvest_season = harvest_season
        self._nutritional_value = 0
        print(f" Harvest season: {self.get_harvest_season()}")
        print(f" Nutritional value: {self.get_nutricional_value()}")

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


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    Rose = Flower("Rose", 15, 10, "red")
    print("[asking the rose to bloom]")
    Rose.bloom()
    Rose.show()
    print()

    Oak = Tree("Oak", 200, 365, 5)
    print("[asking the oak to produce shade]")
    Oak.produce_shade()
    print()

    Tomato = Vegetable("Tomato", 5.0, 10, "April")
    print("[make tomato grow and age for 20 days]")
    Tomato.grow(20)
    Tomato.show()
