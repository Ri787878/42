# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 16:00:16 by ridias            #+#    #+#              #
#    Updated: 2026/03/24 16:03:54 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total() -> None:
	day_1 = int(input("Day 1 harvest: "))
	day_2 = int(input("Day 2 harvest: "))
	day_3 = int(input("Day 3 harvest: "))
	total = int(day_1 + day_2 + day_3)
	print(f"Total harvest: {total}")
