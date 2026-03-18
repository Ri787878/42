#!/usr/bin/env python3

class Plant:
	name: str
	height: int
	age: int

if __name__ == "__main__":
	print(f"=== Garden Plant Registry ===")
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
	print(f"{Rose.name}: {Rose.height}cm, {Rose.age} days old")
	print(f"{Sunflower.name}: {Sunflower.height}cm, {Sunflower.age} days old")
	print(f"{Cactus.name}: {Cactus.height}cm, {Cactus.age} days old")
