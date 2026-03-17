#!/usr/bin/env python3

def ft_plant_age():
	age = int(input("Enter plant age in days: "))
	if age > 60:
		print(f"Plant is ready to harvest!")
	else:
		print(f"Plant needs more time to grow.")
