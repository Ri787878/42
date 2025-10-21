/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/10 15:44:39 by ridias            #+#    #+#             */
/*   Updated: 2025/09/11 12:18:33 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	write_number(int cen, int dez, int uni)
{
	ft_putchar(cen + '0');
	ft_putchar(dez + '0');
	ft_putchar(uni + '0');
	ft_putchar(',');
	ft_putchar(' ');
}

void	ft_print_comb(void)
{
	int	centenas;
	int	dezenas ;
	int	unidades;

	centenas = 0;
	dezenas = 1;
	unidades = 2;
	while (centenas < dezenas && centenas <= 9)
	{
		while (dezenas < unidades && dezenas <= 9)
		{
			while (unidades <= 9)
			{
				write_number(centenas, dezenas, unidades);
				unidades += 1;
			}
			dezenas += 1;
			unidades = dezenas + 1;
		}
		centenas += 1;
		dezenas = centenas + 1;
		unidades = dezenas + 1;
	}
}
