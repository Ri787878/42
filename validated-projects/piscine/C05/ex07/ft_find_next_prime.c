/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_find_next_prime.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/23 14:40:08 by ridias            #+#    #+#             */
/*   Updated: 2025/09/24 15:44:31 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_is_prime(int nb)
{
	int	n;

	n = 2;
	if (nb <= 1)
		return (0);
	while (n <= nb)
	{
		if (nb % n == 0 && n != nb)
			return (0);
		n++;
	}
	return (1);
}

int	ft_find_next_prime(int nb)
{
	int	n;

	n = 2;
	if (nb <= 2)
		return (2);
	while (n <= nb)
	{
		if (ft_is_prime(nb) == 1)
			return (nb);
		nb++;
	}
	return (-1);
}

/*
int main(void)
{
	int i = 15;
	printf("%d = %d\t", i, ft_find_next_prime(i));
	return (0);
}
*/