# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 18:14:20 by ridias            #+#    #+#              #
#    Updated: 2026/03/19 18:14:22 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def ft_plot_area():
	lenght = int(input("Enter lengh: "))
	width = int(input("Enter width: "))
	print(lenght)
	print(width)
	area = int(lenght * width)
	print(f"Plot area: {area}")
