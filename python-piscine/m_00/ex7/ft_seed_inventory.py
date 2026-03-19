# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:14:50 by ridias            #+#    #+#              #
#    Updated: 2026/03/19 18:14:51 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
