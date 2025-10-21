/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/22 17:59:58 by ridias            #+#    #+#             */
/*   Updated: 2025/09/24 15:43:24 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_recursive_factorial(int nb)
{
	int	result;

	result = 1;
	if (nb < 0)
		return (0);
	if (nb == 0)
		return (1);
	if (nb == 1)
		return (1);
	return (nb * ft_recursive_factorial(nb - 1));
}

/*
int main(void)
{
	printf("%d! = %d\n", -1, ft_recursive_factorial(-1));
	printf("%d! = %d\n", 0, ft_recursive_factorial(0));
	printf("%d! = %d\n", 1, ft_recursive_factorial(1));
	printf("%d! = %d\n", 2, ft_recursive_factorial(2));
	printf("%d! = %d\n", 3, ft_recursive_factorial(3));
	printf("%d! = %d\n", 4, ft_recursive_factorial(4));
	printf("%d! = %d\n", 5, ft_recursive_factorial(5));
	return (0);
}
*/