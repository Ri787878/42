# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:14:31 by ridias            #+#    #+#              #
#    Updated: 2026/03/19 18:14:32 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def ft_plant_age():
	age = int(input("Enter plant age in days: "))
	if age > 60:
		print(f"Plant is ready to harvest!")
	else:
		print(f"Plant needs more time to grow.")
