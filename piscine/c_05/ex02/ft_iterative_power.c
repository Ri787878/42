/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/10 17:59:28 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/10 17:59:31 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <math.h>
#include <stdio.h>

int	ft_iterative_power(int nb, int power)
{
	int	n;
	int	count;

	count = nb;
	n = 1;
	if (power < 0)
		return (0);
	if (power == 0)
		return (1);
	while (n < power)
	{
		count = nb * count;
		n++;
	}
	return (count);
}
/*
int	main(void)
{
	printf("%d \n", ft_iterative_power(2, 10));
	return (0);
}
*/
