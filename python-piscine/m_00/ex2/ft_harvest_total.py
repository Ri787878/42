# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:14:27 by ridias            #+#    #+#              #
#    Updated: 2026/03/19 18:40:41 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def ft_harvest_total():
	day_1 = int(input("Day 1 harvest: "))
	day_2 = int(input("Day 2 harvest: "))
	day_3 = int(input("Day 3 harvest: "))
	total = int(day_1 + day_2 + day_3)
	print(f"Total harvest: {total}")


