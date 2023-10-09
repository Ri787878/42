/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/07/25 15:39:43 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/07/26 17:33:39 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	write_num(int num1, int num2, int num3)
{
	write(1, &num1, 1);
	write(1, &num2, 1);
	write(1, &num3, 1);
	write(1, ", ", 2);
}

void	ft_print_comb(void)
{
	char	colum1;
	char	colum2;
	char	colum3;

	colum1 = '0';
	colum2 = '1';
	colum3 = '2';
	while (colum1 <= '6')
	{
		while (colum2 <= '8')
		{
			while (colum3 <= '9')
			{
				if (colum1 < colum2 && colum2 < colum3)
					write_num (colum1, colum2, colum3);
				colum3++;
			}
			colum2++;
			colum3 = colum2 + 1;
		}
		colum1++;
		colum2 = colum1 + 1;
	}
	write (1, "789", 3);
}
