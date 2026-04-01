class Plant:
    name: str
    height: int
    age: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    Rose = Plant()
    Rose.name = "Rose"
    Rose.height = 25
    Rose.age = 30
    Sunflower = Plant()
    Sunflower.name = "Sunflower"
    Sunflower.height = 80
    Sunflower.age = 45
    Cactus = Plant()
    Cactus.name = "Cactus"
    Cactus.height = 15
    Cactus.age = 120

    Rose.show()
    Sunflower.show()
    Cactus.show()
