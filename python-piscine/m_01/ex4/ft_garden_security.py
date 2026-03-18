#!/usr/bin/env python3

class SecurePlant:
	def __init__(self, name):
		self.__name = name
		self.__height = 0
		self.__days = 0
		print(f"Plant created: {name}")

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

