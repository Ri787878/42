# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:12:53 by ridias            #+#    #+#              #
#    Updated: 2026/03/25 16:29:58 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	name: str
	height: float
	age: int

	def __init__(self, name: str, height: float, days: int) -> None:
		self.name = name
		self.height = height
		self.days = days
		self.show()

	def show(self) -> None:
		print(f"Plant created: {self.name}: {round(self.height, 1)}cm, {self.days} days old")

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
		count  = 1
		while count <= days:
			print(f"=== Day {count} ===")
			print(f"{self.name}: {self.height}cm, {self.days} days old")
			self.age()
			self.grow(growth)
			count += 1





if __name__ == "__main__":
	print(f"=== Plant Factory Output ===")

	Rose = Plant("Rose", 25.0, 30)
	Oak = Plant("Oak", 200.0, 365)
	Cactus = Plant("Cactus", 5.0, 90)
	Sunflower = Plant("Sunflower", 80.0, 45)
	Fern = Plant("Fern", 15.0, 120)
	print()
