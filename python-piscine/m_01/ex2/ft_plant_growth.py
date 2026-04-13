class Plant:
    name: str
    height: float
    days: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")

    def grow(self, growth: float) -> None:
        self.height += growth
        self.height = round(self.height, 1)

    def age(self) -> None:
        self.days += 1

    def simulate_growth(self, days: int, growth: float) -> None:
        count = 1
        while count <= days:
            print(f"=== Day {count} ===")
            self.age()
            self.grow(growth)
            print(f"{self.name}: {self.height}cm, {self.days} days old")
            count += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    Rose = Plant()
    Rose.name = "Rose"
    Rose.height = 25.0
    Rose.days = 30
    days_passed = 7
    growth = 0.8
    Rose.show()

    Rose.simulate_growth(days_passed, growth)
    print(f"Growth this week: {round(growth * days_passed, 1)}cm")
