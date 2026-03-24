# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 16:07:39 by ridias            #+#    #+#              #
#    Updated: 2026/03/24 16:07:46 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder() -> None:
	days = int(input("Days since last watering: "))
	if days > 2:
		print(f"Water the plants!")
	else:
		print(f"Plants are fine")
