/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/22 11:32:45 by ridias            #+#    #+#             */
/*   Updated: 2025/09/22 11:46:10 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <limits.h>
#include <unistd.h>

void	ft_putchar(int c)
{
	write(1, &c, 1);
}

int	int_size(int nb)
{
	int	n;

	n = 0;
	while (nb / 10 != 0)
	{
		nb = nb / 10;
		n++;
	}
	return (n);
}

int	ft_pow(int base, int exp)
{
	int	result;

	result = 1;
	while (exp > 0)
	{
		result *= base;
		exp--;
	}
	return (result);
}

int	check_nb(int nb)
{
	if (nb == -2147483648)
	{
		write(1, "-2147483648", 11);
		return (-2147483648);
	}
	if (nb == 0)
	{
		ft_putchar('0');
		return (-2147483648);
	}
	return (nb);
}

void	ft_putnbr(int nb)
{
	int	nb_size;
	int	res;

	nb_size = int_size(nb);
	if (check_nb(nb) == -2147483648)
		return ;
	if (nb < 0)
	{
		ft_putchar('-');
		nb = -nb;
	}
	while (nb_size != 0)
	{
		res = nb / ft_pow(10, nb_size);
		ft_putchar(res + '0');
		nb = nb - res * ft_pow(10, nb_size);
		nb_size--;
	}
	ft_putchar((nb % 10) + '0');
}

/*
int main (void)
{
	int test1 = -42;
	printf("The number %d prints:", test1);
	printf("\n");
	ft_putnbr(test1);

	test1 = INT_MIN;
	printf("\nThe number %d prints:", test1);
	printf("\n");
	ft_putnbr(test1);

	test1 = INT_MAX;
	printf("\nThe number %d prints:", test1);
	printf("\n");
	ft_putnbr(test1);

	test1 = 0;
	printf("\nThe number %d prints:", test1);
	printf("\n");
	ft_putnbr(test1);
	return (0);
}
*/