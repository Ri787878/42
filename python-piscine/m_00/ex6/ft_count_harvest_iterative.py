# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 16:08:52 by ridias            #+#    #+#              #
#    Updated: 2026/03/24 16:10:52 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative() -> None:
	days = int(input("Days until harvest: "))
	for i in range(days):
		print(f"Day {i + 1}")
		if i + 1 == days:
			print(f"Harvest time!")
