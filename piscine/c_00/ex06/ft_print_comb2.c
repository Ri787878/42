/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb2.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/07/26 16:59:39 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/07/27 10:00:40 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	write_num(int num1, int num2)
{
	char	c;

	c = (num1 / 10) + '0';
	write(1, &c, 1);
	c = (num1 % 10) + '0';
	write(1, &c, 1);
	write(1, " ", 1);
	c = (num2 / 10) + '0';
	write(1, &c, 1);
	c = (num2 % 10) + '0';
	write(1, &c, 1);
	write(1, ", ", 2);
}

void	ft_print_comb2(void)
{
	int	colum1;
	int	colum2;

	colum1 = 0;
	colum2 = 1;
	while (colum1 < 98)
	{
		while (colum2 <= 99)
		{
			if (colum1 == colum2)
			{
				colum2++;
			}
			write_num(colum1, colum2);
			colum2++;
		}
		colum1++;
		colum2 = colum1 + 1;
	}
	write(1, "98 99", 5);
}
