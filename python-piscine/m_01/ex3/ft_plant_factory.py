# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:12:53 by ridias            #+#    #+#              #
#    Updated: 2026/03/19 18:12:54 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

class Plant:
	def __init__(self, name, height, days):
		self.name = name
		self.height = height
		self.days = days
		print(f"Created: {self.name} ({self.height}cm, {self.days} days)")

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
	print(f"=== Plant Factory Output ===")

	Rose = Plant("Rose", 25, 30)
	Oak = Plant("Oak", 200, 365)
	Cactus = Plant("Cactus", 5, 90)
	Sunflower = Plant("Sunflower", 80, 45)
	Fern = Plant("Fern", 15, 120)
	print()
	print(f"Total plants created: 5")
