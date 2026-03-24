# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:14:50 by ridias            #+#    #+#              #
#    Updated: 2026/03/24 16:17:25 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if unit == "packets":
		print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
	elif unit == "grams":
		print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
	elif unit == "area":
		print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
	else:
		print(f"Unknown unit type")

if __name__ == "__main__":
	ft_seed_inventory("tomato", 15, "packets")
	print()
	ft_seed_inventory("carrot", 8, "grams")
	print()
	ft_seed_inventory("lettuce", 12, "area")
	print()
