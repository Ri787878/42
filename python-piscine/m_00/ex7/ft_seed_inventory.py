#!/usr/bin/env python3

def ft_seed_inventory(vegetable, nbr, unit):
	if unit == "packets":
		print(f"{vegetable.capitalize()} seeds: {nbr} {unit} available")
	if unit == "grams":
		print(f"{vegetable.capitalize()} seeds: {nbr} {unit} total")
	if unit == "area":
		print(f"{vegetable.capitalize()} seeds: covers {nbr} square meters")
	else:
		print(f"Unknown unit type")
