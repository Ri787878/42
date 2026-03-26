# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:12:56 by ridias            #+#    #+#              #
#    Updated: 2026/03/26 14:11:04 by ridias           ###   ########.fr        #
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

if __name__ == "__main__":
	print(f"=== Garden Security System ===")

	Rose = Plant("Rose", 15.0, 10)
	print()
	Rose.set_height(25)
	Rose.set_age(30)
	print()
	Rose.set_height(-5.0)
	Rose.set_age(-5.0)
	print()
	Rose.show()
