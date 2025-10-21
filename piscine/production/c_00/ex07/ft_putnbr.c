/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/11 11:16:55 by ridias            #+#    #+#             */
/*   Updated: 2025/09/18 17:09:07 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

int	int_number_counter(int n)
{
	int	count;

	count = 0;
	while (n != 0)
	{
		n /= 10;
		count += 1;
	}
	return (count);
}

int	ft_power(int base, int exp)
{
	int	total;

	total = 1;
	while (exp != 0)
	{
		total *= base;
		exp--;
	}
	return (total);
}

int	test_number(int nb)
{
	int	res;

	res = 0;
	if (nb < 0)
	{
		res = -nb;
		ft_putchar('-');
	}
	return (res);
}

void	ft_putnbr(int nb)
{
	int	n;
	int	nb_lenght;
	int	res;

	nb_lenght = int_number_counter(nb);
	n = 1;
	if (nb == -2147483647)
	{
		write(1, "-2147483647", 11);
		return ;
	}
	if (nb == 0)
	{
		ft_putchar('0');
		return ;
	}
	if (nb < 0)
		nb = test_number(nb);
	while (n <= nb_lenght)
	{
		res = nb / ft_power(10, nb_lenght - n);
		ft_putchar(res + '0');
		nb = nb - (res * ft_power(10, nb_lenght - n));
		n += 1;
	}
}
