/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_fibonacci.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/10 18:22:24 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/10 18:22:27 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <math.h>
#include <stdio.h>

int	ft_fibonacci(int index)
{
	int	count;
	int	min;

	min = -1;
	count = index;
	if (index < 0)
		return (min);
	if (index == 0)
		return (0);
	if (index == 1)
		return (1);
	if (index == 2)
		return (1);
	if (index > 2)
		count = ft_fibonacci(index - 1) + ft_fibonacci(index - 2);
	return (count);
}
/*
int	main(void)
{
	printf("%d \n", ft_fibonacci(20));
	return (0);
}
*/
