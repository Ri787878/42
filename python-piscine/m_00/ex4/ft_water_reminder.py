#!/usr/bin/env python3

def ft_water_reminder():
	days = int(input("Days since last watering: "))
	if days > 2:
		print(f"Water the plants!")
	else:
		print(f"Plants are fine")
