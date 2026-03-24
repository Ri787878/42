# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:12:56 by ridias            #+#    #+#              #
#    Updated: 2026/03/24 19:22:27 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3
class Plant:
	name: str
	height: float
	age: int

	def __init__(self, name: str) -> None:
		self.__name = name
		self.__height = 0
		self.__days = 0
		print(f"Created: {self.name} {round(self.__height, 1)}cm, {self.__days} days old")

	def show(self) -> None:
		print(f"{self.name}: {self.height}cm, {self.age} days old")

	def grow(self, growth: int) -> None:
		self.height += growth
		self.height = round(self.height, 1)

	def age(self) -> None:
		self.days += 1

	def set_height(self, height):
		if height >= 0:
			self.__height = height
			print(f"Height updated: {height}cm [OK]")
		else:
			print(f"Invalid operation attempted: height {height}cm [REJECTED]")
			print(f"Security: Negative height rejected")

	def set_age(self, age):
		if age >= 0:
			self.__days = age
			print(f"Age updated: {age} days [OK]")
		else:
			print(f"Invalid operation attempted: age {age}cm [REJECTED]")
			print(f"Security: Negative age rejected")

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

class SecurePlant:
	def __init__(self, name):
		self.__name = name
		self.__height = 0
		self.__days = 0
		print(f"Plant created: {name}")



	def get_info(self):
		print(f"Current plant: {self.__name} ({self.__height}cm, {self.__days} days)")

if __name__ == "__main__":
	print(f"=== Garden Security System ===")

	Rose = SecurePlant("Rose")
	Rose.set_height(25)
	Rose.set_age(30)
	print()
	Rose.set_height(-5)
	print()
	Rose.get_info()

