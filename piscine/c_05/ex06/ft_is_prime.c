/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_is_prime.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/10 19:30:07 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/14 11:50:07 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <math.h>
#include <stdio.h>

int	ft_is_prime(int nb)
{
	int	i;
	int	count;

	i = 3;
	count = 0;
	if (nb % 2 == 0)
		return (0);
	while (i * i <= nb && i < 46342)
	{
		if (nb % i == 0)
		{
			count = 1;
			break ;
		}
		i = i + 2;
	}
	if (count == 0)
		return (1);
	return (0);
}
/*
int	main(void)
{
	int	n1;

	n1 =   23546578;
	printf("num %d, is %d\n", n1, ft_is_prime(n1));
	return (0);
}
*/
