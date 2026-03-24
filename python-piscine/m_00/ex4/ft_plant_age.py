# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 16:03:20 by ridias            #+#    #+#              #
#    Updated: 2026/03/24 16:05:04 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age() -> None:
	age = int(input("Enter plant age in days: "))
	if age > 60:
		print(f"Plant is ready to harvest!")
	else:
		print(f"Plant needs more time to grow.")
