/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ljorge-r <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/15 08:36:27 by ljorge-r          #+#    #+#             */
/*   Updated: 2023/08/15 08:36:29 by ljorge-r         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

int	*ft_range(int min, int max)
{
	int	i;
	int	*result;

	if (min >= max)
		return (NULL);
	i = max - min;
	result = (int *)malloc(sizeof(int) * (i));
	if (result == NULL)
	{
		return (NULL);
	}
	i = 0;
	while (max > min)
	{
		result[i] = min;
		min++;
		i++;
	}
	return (result);
}
/*
int	main(void)
{
	int	min;
	int	max;
	int	*array;
	int	i = 0;
	int	size;

	min = 5;
	max = 10;
	size = max - min;
	array = ft_range(min, max);
	while(i < size)
	{
		printf("%d, ", array[i]);
		i++;
	}
}*/
