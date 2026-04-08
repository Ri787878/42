/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/23 12:07:20 by ridias            #+#    #+#             */
/*   Updated: 2025/09/24 15:43:34 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_iterative_power(int nb, int power)
{
	int	result;

	result = 1;
	if (power < 0)
		return (0);
	while (power > 0)
	{
		result *= nb;
		power--;
	}
	return (result);
}

/*
int main(void)
{
	printf("%d = %d\n", 0, ft_iterative_power(0, 0));
	printf("%d = %d\n", 1, ft_iterative_power(1, 1));
	printf("%d = %d\n", 2, ft_iterative_power(2, 3));
	printf("%d = %d\n", 3, ft_iterative_power(5, 3));
	printf("%d = %d\n", 4, ft_iterative_power(10, 4));
	return (0);
}
*/