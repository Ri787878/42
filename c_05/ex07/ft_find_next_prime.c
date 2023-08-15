/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_find_next_prime.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/15 12:05:22 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/15 12:05:27 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <math.h>
#include <stdio.h>

int	ft_is_prime(int nb)
{
	int	i;
	int	count;

	i = 3;
	count = 0;
	if ((nb % 2 == 0 || nb < 0) && nb != 2)
		return (0);
	while (i * i <= nb && i < 46342)
	{
		if (nb % i == 0)
			return (0);
		i = i + 2;
	}
	return (1);
}

int	ft_find_next_prime(int nb)
{
	while (nb < 2147483647 && !ft_is_prime(nb))
	{
		nb++;
	}
	return (nb);
}
/*
int main(void)
{
	printf("O proximo prime e %d.\n", ft_find_next_prime(-10));
	printf("O proximo prime e %d.\n", ft_find_next_prime(-1));
	printf("O proximo prime e %d.\n", ft_find_next_prime(0));
	printf("O proximo prime e %d.\n", ft_find_next_prime(1));
	printf("O proximo prime e %d.\n", ft_find_next_prime(2));
	printf("O proximo prime e %d.\n", ft_find_next_prime(3));
	printf("O proximo prime e %d.\n", ft_find_next_prime(12));
	printf("O proximo prime e %d.\n", ft_find_next_prime(21474836));
	return (0);
}
*/
