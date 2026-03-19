# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:14:43 by ridias            #+#    #+#              #
#    Updated: 2026/03/19 18:14:44 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def recursive_helper(days, i):
	print(f"Day {i}")
	if i == days:
		print(f"Harvest time!")
	else:
		recursive_helper(days, i + 1)

def ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	recursive_helper(days, 1)
