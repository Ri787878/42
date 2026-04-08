class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = height
        self._days = days
        print(
            f"Plant created: {self._name}:"
            + f"{self._height:.1f}cm, {self._days} days old")

    def show(self) -> None:
        print(
            f"Current state: {self._name}:"
            + f"{self._height:.1f}cm, {self._days} days old")

    def grow(self, growth: int) -> None:
        self._height += growth
        self._height = round(self._height, 1)

    def age(self) -> None:
        self._days += 1

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._days = age
            print(f"Age updated: {age} days")
        else:
            print("Rose: Error, age can't be negative")
            print("Age update rejected")

    def simulate_growth(self, days: int, growth: int) -> None:
        count = 1
        while count <= days:
            print(f"=== Day {count} ===")
            print(f"{self._name}: {self._height}cm, {self._days} days old")
            self.age()
            self.grow(growth)
            count += 1


if __name__ == "__main__":
    print("=== Garden Security System ===")

    Rose = Plant("Rose", 15.0, 10)
    print()
    Rose.set_height(25)
    Rose.set_age(30)
    print()
    Rose.set_height(-5.0)
    Rose.set_age(-5)
    print()
    Rose.show()
