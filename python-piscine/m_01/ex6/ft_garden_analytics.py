# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:13:03 by ridias            #+#    #+#              #
#    Updated: 2026/03/26 20:24:07 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

class Plant:
	class Stats():
		def __init__(self):
			self._grows_calls = 0
			self._age_calls = 0
			self._show_calls = 0

		def get_grow_calls(self) -> int:
			return self._grows_calls
		def get_age_calls(self) -> int:
			return self._age_calls
		def get_show_calls(self) -> int:
			return self._show_calls

		def increase_grow_call(self) -> None:
			self._grows_calls += 1

		def increase_age_call(self) -> None:
			self._age_calls += 1

		def increase_show_call(self) -> None:
			self._show_calls += 1


	def __init__(self, name: str, height: float, days: int) -> None:
		self._name = name
		self._height = height
		self._inicial_height = height
		self._days = days
		self._stats = self.Stats()
		print(f"{self._name}: {self._height:.1f}cm, {self._days} days old")

	def show(self) -> None:
		print(f"{self._name}: {self._height:.1f}cm, {self._days} days old")
		self._stats.increase_show_call()

	def grow(self, days: int) -> None:
		total_growth: float
		total_growth = 2.1 * days
		self._height += total_growth
		self.age(days)
		self._height = round(self._height, 1)
		self._stats.increase_grow_call()

	def age(self, days:int) -> None:
		self._days += days
		self._stats.increase_age_call()

	def set_height(self, height: float):
		if height >= 0:
			self._height = height
			print(f"Height updated: {height}cm")
		else:
			print(f"{self._name}: height can't be negative")
			print(f"Height update rejected")

	def set_age(self, age):
		if age >= 0:
			self._days = age
			print(f"Age updated: {age} days")
		else:
			print(f"Rose: Error, age can't be negative")
			print(f"Age update rejected")

	def get_name(self) -> str:
			return self._name

	def get_days(self) -> int:
			return self._days

	def get_height(self) -> float:
			return self._height

	def simulate_growth(self, days: int, growth: int) -> None:
		count  = 1
		while count <= days:
			print(f"=== Day {count} ===")
			print(f"{self._name}: {self._height}cm, {self._days} days old")
			self.age()
			self.grow(growth)
			count += 1

	@staticmethod
	def valid_age(days: int) -> bool:
		if days >365:
			return True
		else:
			return False
	@classmethod
	def create_anonymous(cls, name):
		return cls(name, 0, 0)

class Flower(Plant):
	def __init__(self, name, height, days, color):
		print(f"=== Flower")
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
		return	self._color

	def show(self) -> None:
		super().show()
		print(f" Color: {self.get_color()}")
		self.is_blomming()

class Seed(Flower):
	def __init__(self, name, height, days, color, total_seeds):
		self._total_seeds = total_seeds
		super().__init__(name, height, days, color)
	def get_total_seeds(self) -> int:
		return self._total_seeds
	def show(self) -> None:
		super().show()
		print(f" Seeds: {self.get_total_seeds()}")

	def set_seeds(self, seeds) -> None:
		if self.bloom:
			self._total_seeds = seeds
		else:
			return



class Tree(Plant):
	def __init__(self, name, height, days, trunk_size):
		print(f"=== Tree")
		super().__init__(name, height, days)
		self._trunk_diameter = trunk_size
		print(f" Trunk diameter: {self.get_trunk_diameter():.1f}cm")

	def produce_shade(self):
		print(f"Tree {self.get_name()} now produces a shade of {self.get_height():.1f}cm long and {self.get_trunk_diameter():.1f}cm wide.")

	def get_trunk_diameter(self) -> float:
		return	self._trunk_diameter

	def show(self) -> None:
		super().show()
		print(f" Trunk diameter: {self.get_trunk_diameter():.1f}cm")

class Vegetable(Plant):
	def __init__(self, name, height, days, harvest_season):
		print(f"=== Vegetable")
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
		return	self._harvest_season

	def get_nutricional_value(self) -> int:
		return	self._nutritional_value

	def increase_nutricional_value(self, nutricional_value: int) -> None:
		self._nutritional_value += nutricional_value

	def show(self) -> None:
		super().show()
		print(f" Harvest season: {self.get_harvest_season()}")
		print(f" Nutritional value: {self.get_nutricional_value()}")


def show_stats(plant: Plant) -> None:
	print(f"Stats: {plant._stats.get_grow_calls()} grow, {plant._stats.get_age_calls()} age, {plant._stats.get_show_calls()} show")
	#Stats: 1 grow, 0 age, 2 show
if __name__ == "__main__":
	print(f"=== Garden statistics ===")
	#oak = Tree("Oak Tree", 101, 0)
	Rose = Flower("Rose", 15, 10, "red")
	#stat_manager = Plant().
	show_stats(Rose)
	print()
	Rose.grow(5)
	show_stats(Rose)
