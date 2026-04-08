/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_is_prime.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/23 14:27:45 by ridias            #+#    #+#             */
/*   Updated: 2025/09/24 15:44:17 by ridias           ###   ########.fr       */
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

/*
int main(void)
{
	int i = -1;
	while (i <= 1000)
	{
		if (ft_is_prime(i) != 0)
			printf("%d = %d\t", i, ft_is_prime(i));
		if (i % 10 == 0)
			printf("\n");
		i++;
	}
	return (0);
}
*/