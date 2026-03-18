#!/usr/bin/env python3

class GardenManager():
	def __init__(self, name):
		self.name = name
		self.Garden = Garden(name)

	def add_plant(self, plant_instance):
		self.garden.add_to_stock(plant_instance)

	def garden_report(self):
		print(f"=== {self.Garden.name}'s Garden Report ===")
		print(f"Plants in garden:")
		for plant in self.Garden.plant_stock:
			if

	class GardensStats:
		@classmethod
		def count_regular_plants(self):
			pass

class Garden():
	def __init__(self, garden_owner_name):
		self.plant_stock = []
		self.total_plants = 0
		self.regular_plants_stock = 0
		self.flowering_plants_stock = 0
		self.prize_flower_stock = 0
		self.name = garden_owner_name

	def add_to_stock(self, plant_instance):
		self.plant_stock.append(plant_instance)
		self.total_plants += 1
		print(f"Added {plant_instance.name} to {self.name}'s garden")


class Plant(Garden):
	def __init__(self, garden_owner_name, plant_name, height, days):
		super().__init__(self, garden_owner_name)
		self.inicial_height = height
		self.height = height
		self.days = days
		self.add_to_stock(self, plant_name)

	def __str__(self):
		return super().__str__()

	def grow(self, growth: int):
		self.height += growth

	def age(self, days):
		self.days += days

	def current_growth(self):
		for plant in self.plant_stock:
			growth = self.height - self.inicial_height
			print(f"123")

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

class FloweringPlant(Plant):
	def __init__(self, garden_owner_name, plant_name, height, days):
		super().__init__(garden_owner_name, plant_name, height, days)
		self.flowering_plants += 1

class PrizeFlower(FloweringPlant):
	def __init__(self, garden_owner_name, plant_name, height, days):
		super().__init__(garden_owner_name, plant_name, height, days)
		self.prize_flower += 1


	def create_garden_network():
		pass



if __name__ == "__main__":
	print(f"=== Garden Management System Demo ===")
	Alice = GardenManager("Alice")
	Alice.add_plant("Oak Tree")
	Alice.add_plant("Rose")
	Alice.add_plant("Sunflower")


#Added Oak Tree to Alice's garden
#Added Rose to Alice's garden
#Added Sunflower to Alice's garden
#Alice is helping all plants grow...
#Oak Tree grew 1cm
#Rose grew 1cm
#Sunflower grew 1cm
#=== Alice's Garden Report ===
#Plants in garden:
#- Oak Tree: 101cm
#- Rose: 26cm, red flowers (blooming)
#- Sunflower: 51cm, yellow flowers (blooming), Prize points: 10
#Plants added: 3, Total growth: 3cm
#Plant types: 1 regular, 1 flowering, 1 prize flowers
#Height validation test: True
#Garden scores - Alice: 218, Bob: 92
#Total gardens managed: 2
