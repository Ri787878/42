class Plant:
    name: str
    height: float
    age: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, growth: int) -> None:
        self.height += growth
        self.height = round(self.height, 1)

    def age(self) -> None:
        self.days += 1

    def get_info(self, info: str) -> None:
        if info == "name":
            return self.name
        if info == "days":
            return self.days
        if info == "height":
            return self.height

    def simulate_growth(self, days: int, growth: int) -> None:
        count = 1
        while count <= days:
            print(f"=== Day {count} ===")
            print(f"{self.name}: {self.height}cm, {self.days} days old")
            self.age()
            self.grow(growth)
            count += 1


if __name__ == "__main__":
    Rose = Plant()
    Rose.name = "Rose"
    Rose.height = 25
    Rose.days = 30
    days_passed = 7
    growth = 0.8

    Rose.simulate_growth(days_passed, growth)
    print(f"Growth this week: {round(growth * days_passed)}cm")
