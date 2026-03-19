# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:14:40 by ridias            #+#    #+#              #
#    Updated: 2026/03/19 18:14:41 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def ft_count_harvest_iterative():
	days = int(input("Days until harvest: "))
	for i in range(days):
		print(f"Day {i + 1}")
		if i + 1 == days:
			print(f"Harvest time!")
