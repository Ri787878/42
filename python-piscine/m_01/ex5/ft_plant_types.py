# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:13:01 by ridias            #+#    #+#              #
#    Updated: 2026/03/25 17:14:01 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

class Plant:
	def __init__(self, name: str, height: float, days: int) -> None:
		self.__name = name
		self.__height = height
		self.__days = days
		print(f"Plant created: {self.__name}: {self.__height:.1f}cm, {self.__days} days old")

	def show(self) -> None:
		print(f"Current state: {self.__name}: {self.__height:.1f}cm, {self.__days} days old")

	def grow(self, growth: int) -> None:
		self.__height += growth
		self.__height = round(self.__height, 1)

	def age(self) -> None:
		self.__days += 1

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

	def get_info(self, info: str) -> None:
		if info == "name":
			return self.__name
		if info == "days":
			return self.__days
		if info == "height":
			return self.__height

	def simulate_growth(self, days: int, growth: int) -> None:
		count  = 1
		while count <= days:
			print(f"=== Day {count} ===")
			print(f"{self.__name}: {self.__height}cm, {self.__days} days old")
			self.age()
			self.grow(growth)
			count += 1

class Flower(Plant):
	def __init__(self, name, height, days, color):
		super().__init__(name, height, days)
		self.color = color

	def bloom(self):
		print(f"{self.name} is blooming beautifully!")

class Tree(Plant):
	def __init__(self, name, height, days, trunk_size):
		super().__init__(name, height, days)
		self.trunk_diameter = trunk_size

	def produce_shade(self):
		#r = (self.trunk_diameter) / 2
		trunk_meters = self.trunk_diameter / 100
		crown = 20 * trunk_meters
		radius = crown / 2
		shade = (radius ** 2) * 3.12
		print(f"Oak provides {int(shade)} square meters of shade")

class Vegetable(Plant):
	def __init__(self, name, height, days, harvest_season, nutritional_value):
		super().__init__(name, height, days)
		self.harvest_season = harvest_season
		self.nutritional_value = nutritional_value

if __name__ == "__main__":
	print(f"=== Garden Plant Types ===")

	Rose = Flower("Rose", 25, 30, "red")
	Rose.get_info()
	Rose.bloom()
	print()
	Oak = Tree("Oak", 500, 1825, 50)
	Oak.get_info()
	Oak.produce_shade()
	print()
	Tomato = Vegetable("Tomato", 80, 90, "summer", "C")
	Tomato.get_info()
	print()

	Poppy = Flower("Poppy", 20, 15, "White")
	Maple = Tree("Maple", 1000, 2000, 150)
	Cucumber = Vegetable("Cucumber", 65, 55, "Spring", "B1")
	print()
