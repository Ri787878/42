# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:13:01 by ridias            #+#    #+#              #
#    Updated: 2026/03/19 18:13:02 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

class Plant:
	def __init__(self, name, height, days):
		self.name = name
		self.height = height
		self.days = days
	def grow(self, growth: int):
		self.height += growth

	def age(self, days):
		self.days += days

class Flower(Plant):
	def __init__(self, name, height, days, color):
		super().__init__(name, height, days)
		self.color = color

	def bloom(self):
		print(f"{self.name} is blooming beautifully!")

	def get_info(self):
		print(f"{self.name} (Flower): {self.height}cm, {self.days} days, {self.color} color")

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

	def get_info(self):
		print(f"{self.name} (Tree): {self.height}cm, {self.days} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
	def __init__(self, name, height, days, harvest_season, nutritional_value):
		super().__init__(name, height, days)
		self.harvest_season = harvest_season
		self.nutritional_value = nutritional_value
	def get_info(self):
		print(f"{self.name} (Vegetable): {self.height}cm, {self.days} days, {self.harvest_season} harvest")
		print(f"{self.name} is rich in {self.nutritional_value}")




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
