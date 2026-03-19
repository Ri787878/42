# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:14:46 by ridias            #+#    #+#              #
#    Updated: 2026/03/19 18:14:47 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def ft_garden_summary():
	garden_name = input("Enter garden name: ")
	plant_number = input("Enter number of plants: ")
	print(f"Garden: {garden_name}")
	print(f"Plants: {plant_number}")
	print(f"Status: Growing well!")
