#!/usr/bin/env python3

class Plant:
	name: str
	height: int
	days: int

	def grow(self, growth: int):
		self.height += growth

	def age(self, days):
		self.days += days

	def get_info(self, info: str):
		if info == "name":
			return self.name
		if info == "days":
			return self.days
		if info == "height":
			return self.height





if __name__ == "__main__":
	Rose = Plant()
	Rose.name = "Rose"
	Rose.height = 25
	Rose.days = 30
	days_passed = 6

	print(f"=== Day 1 ===")
	print(f"{Rose.name}: {Rose.height}cm, {Rose.days} days old")
	Rose.age(days_passed)
	Rose.grow(days_passed)

	print(f"=== Day {1 + days_passed} ===")
	print(f"{Rose.name}: {Rose.height}cm, {Rose.days} days old")
	print(f"Growth this week: +{days_passed}cm")
