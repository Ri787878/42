/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/10 18:35:00 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/10 18:35:05 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <math.h>
#include <stdio.h>

int	ft_recursive_factorial(int nb)
{
	int	n;
	int	count;

	count = 1;
	n = 1;
	if (nb < 0)
		return (0);
	if (nb == 0)
		return (1);
	if (nb > 0)
		count = ft_recursive_factorial(nb - 1) * nb;
	return (count);
}
/*
int	main(void)
{
	int	c1;

	c1 = 10;
	printf("%d \n", ft_recursive_factorial(c1));
	return (0);
}
*/
