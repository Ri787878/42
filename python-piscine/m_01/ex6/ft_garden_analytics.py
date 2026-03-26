# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:13:03 by ridias            #+#    #+#              #
#    Updated: 2026/03/26 18:41:00 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

class Plant:
	def __init__(self, name: str, height: float, days: int) -> None:
		self.__name = name
		self.__height = height
		self.__inicial_height = height
		self.__days = days
		print(f"{self.__name}: {self.__height:.1f}cm, {self.__days} days old")

	def show(self) -> None:
		print(f"{self.__name}: {self.__height:.1f}cm, {self.__days} days old")

	def grow(self, days: int) -> None:
		total_growth: float
		total_growth = 2.1 * days
		self.__height += total_growth
		self.age(days)
		self.__height = round(self.__height, 1)

	def age(self, days:int) -> None:
		self.__days += days

	def set_height(self, height: float):
		if height >= 0:
			self.__height = height
			print(f"Height updated: {height}cm")
		else:
			print(f"{self.__name}: height can't be negative")
			print(f"Height update rejected")

	def set_age(self, age):
		if age >= 0:
			self.__days = age
			print(f"Age updated: {age} days")
		else:
			print(f"Rose: Error, age can't be negative")
			print(f"Age update rejected")

	def get_name(self) -> str:
			return self.__name

	def get_days(self) -> int:
			return self.__days

	def get_height(self) -> float:
			return self.__height

	def simulate_growth(self, days: int, growth: int) -> None:
		count  = 1
		while count <= days:
			print(f"=== Day {count} ===")
			print(f"{self.__name}: {self.__height}cm, {self.__days} days old")
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

	class Stats():
		grows_calls = 0
		age_calls = 0
		show_calls = 0
		
		def get_

class Flower(Plant):
	def __init__(self, name, height, days, color):
		print(f"=== Flower")
		super().__init__(name, height, days)
		self.__color = color
		self.__bloom = False
		print(f" Color: {self.get_color()}")
		self.is_blomming()

	def bloom(self) -> None:
		if (self.__bloom):
			return
		else:
			self.__bloom = True

	def is_blomming(self) -> None:
		if (self.__bloom):
			print(f" {self.get_name()} is blooming beautifully!")
		else:
			print(f" {self.get_name()} has not bloomed yet")

	def get_color(self) -> str:
		return	self.__color

	def show(self) -> None:
		super().show()
		print(f" Color: {self.get_color()}")
		self.is_blomming()

class Seed(Flower):
	def __init__(self, name, height, days, color, total_seeds):
		self.__total_seeds = total_seeds
		super().__init__(name, height, days, color)
	def get_total_seeds(self) -> int:
		return self.__total_seeds
	def show(self) -> None:
		super().show()
		print(f" Seeds: {self.get_total_seeds()}")

	def set_seeds(self, seeds) -> None:
		if self.bloom:
			self.__total_seeds = seeds
		else:
			return



class Tree(Plant):
	def __init__(self, name, height, days, trunk_size):
		print(f"=== Tree")
		super().__init__(name, height, days)
		self.__trunk_diameter = trunk_size
		print(f" Trunk diameter: {self.get_trunk_diameter():.1f}cm")

	def produce_shade(self):
		print(f"Tree {self.get_name()} now produces a shade of {self.get_height():.1f}cm long and {self.get_trunk_diameter():.1f}cm wide.")

	def get_trunk_diameter(self) -> float:
		return	self.__trunk_diameter

	def show(self) -> None:
		super().show()
		print(f" Trunk diameter: {self.get_trunk_diameter():.1f}cm")

class Vegetable(Plant):
	def __init__(self, name, height, days, harvest_season):
		print(f"=== Vegetable")
		super().__init__(name, height, days)
		self.__harvest_season = harvest_season
		self.__nutritional_value = 0
		print(f" Harvest season: {self.get_harvest_season()}")
		print(f" Nutritional value: {self.get_nutricional_value()}")

	def grow(self, days: int) -> None:
		super().grow(days)

	def age(self, days: int) -> None:
		super().age(days)
		self.increase_nutricional_value(days)

	def get_harvest_season(self) -> str:
		return	self.__harvest_season

	def get_nutricional_value(self) -> int:
		return	self.__nutritional_value

	def increase_nutricional_value(self, nutricional_value: int) -> None:
		self.__nutritional_value += nutricional_value

	def show(self) -> None:
		super().show()
		print(f" Harvest season: {self.get_harvest_season()}")
		print(f" Nutritional value: {self.get_nutricional_value()}")


if __name__ == "__main__":
	print(f"=== Garden statistics ===")
	#oak = Tree("Oak Tree", 101, 0)
	Rose = Flower("Rose", 15, 10, "red")
	stat_manager = Plant().

