# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:14:35 by ridias            #+#    #+#              #
#    Updated: 2026/03/19 18:14:36 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def ft_water_reminder():
	days = int(input("Days since last watering: "))
	if days > 2:
		print(f"Water the plants!")
	else:
		print(f"Plants are fine")
