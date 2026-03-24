# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#     ft_plot_area.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 15:57:07 by ridias            #+#    #+#              #
#    Updated: 2026/03/24 16:03:44 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area() -> None:
	lenght = int(input("Enter lengh: "))
	width = int(input("Enter width: "))
	print(lenght)
	print(width)
	area = int(lenght * width)
	print(f"Plot area: {area}")
