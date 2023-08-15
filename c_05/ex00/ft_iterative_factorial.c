/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/10 17:53:15 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/10 17:53:18 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <math.h>
#include <stdio.h>

int	ft_iterative_factorial(int nb)
{
	int	n;
	int	count;

	count = 1;
	n = 1;
	if (nb < 0)
		return (0);
	if (nb == 0)
		return (1);
	while (n <= nb)
	{
		count = count * n;
		n++;
	}
	return (count);
}
/*
int	main(void)
{
	int	c1;

	c1 = 10;
	printf("%d \n", ft_iterative_factorial(c1));
	return (0);
}
*/
