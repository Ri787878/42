/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/23 12:15:28 by ridias            #+#    #+#             */
/*   Updated: 2025/09/23 15:06:40 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_recursive_power(int nb, int power)
{
	if (power < 0)
		return (0);
	if (power == 0)
		return (1);
	if (power == 1)
		return (nb);
	return (nb * ft_recursive_power(nb, power - 1));
}

/*
int main(void)
{
	printf("0**1 = %d\n", ft_recursive_power(0, 1));
	printf("1**1 = %d\n", ft_recursive_power(1, 1));
	printf("2**3 = %d\n", ft_recursive_power(2, 3));
	printf("5**3 = %d\n", ft_recursive_power(5, 3));
	printf("10**4 = %d\n", ft_recursive_power(10, 4));
	return (0);
}
*/