/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/10 18:21:59 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/10 18:22:08 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <math.h>
#include <stdio.h>

int	ft_recursive_power(int nb, int power)
{
	int	n;
	int	count;

	count = nb;
	n = 1;
	if (power < 0)
		return (0);
	if (power == 0)
		return (1);
	if (power == 1)
		return (nb);
	if (power > 1)
		count = nb * ft_recursive_power(nb, power - 1);
	return (count);
}
/*
int	main(void)
{
	printf("%d \n", ft_recursive_power(6, 10));
	return (0);
}
*/
