/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/22 17:36:06 by ridias            #+#    #+#             */
/*   Updated: 2025/09/24 15:43:13 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_iterative_factorial(int nb)
{
	int	result;

	result = 1;
	if (nb < 0)
		return (0);
	if (nb == 0)
		return (1);
	while (nb > 0)
	{
		result *= nb;
		nb--;
	}
	return (result);
}

/*
int main (void)
{
	printf("%d! = %d\n", -1, ft_iterative_factorial(-1));
	printf("%d! = %d\n", 0, ft_iterative_factorial(0));
	printf("%d! = %d\n", 1, ft_iterative_factorial(1));
	printf("%d! = %d\n", 2, ft_iterative_factorial(2));
	printf("%d! = %d\n", 3, ft_iterative_factorial(3));
	printf("%d! = %d\n", 4, ft_iterative_factorial(4));
	printf("%d! = %d\n", 5, ft_iterative_factorial(5));
	return (0);
}
*/