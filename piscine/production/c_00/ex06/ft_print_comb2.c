/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb2.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/10 15:49:10 by ridias            #+#    #+#             */
/*   Updated: 2025/09/11 12:18:42 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	write_number2(int num1, int num2)
{
	int	mil;
	int	cen;
	int	dez;
	int	uni;

	mil = num1 / 10;
	cen = num1 % 10;
	dez = num2 / 10;
	uni = num2 % 10;
	ft_putchar(mil + '0');
	ft_putchar(cen + '0');
	ft_putchar(' ');
	ft_putchar(dez + '0');
	ft_putchar(uni + '0');
	if (num1 != 98)
		write(1, ", ", 2);
}

void	ft_print_comb2(void)
{
	int	num1;
	int	num2;

	num1 = 0;
	num2 = 1;
	while (num1 < num2)
	{
		while (num2 <= 99)
		{
			write_number2(num1, num2);
			num2 += 1;
		}
		num1 += 1;
		num2 = num1 + 1;
	}
}
