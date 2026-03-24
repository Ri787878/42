# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 16:09:04 by ridias            #+#    #+#              #
#    Updated: 2026/03/24 16:10:33 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def recursive_helper(days: int, i: int) -> None:
	print(f"Day {i}")
	if i == days:
		print(f"Harvest time!")
	else:
		recursive_helper(days, i + 1)

def ft_count_harvest_recursive() -> None:
	days = int(input("Days until harvest: "))
	recursive_helper(days, 1)
