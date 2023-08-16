/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_range.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/16 11:39:54 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/16 11:39:57 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>

int	ft_ultimate_range(int **range, int min, int max)
{
	int	i;
	int	*result;

	if (min >= max)
	{
		*range = NULL;
		return (0);
	}
	i = max - min;
	result = (int *)malloc(sizeof(int) * (i));
	if (result == NULL)
	{
		*range = NULL;
		return (-1);
	}
	*range = result;
	i = 0;
	while (max > min)
	{
		result[i] = min;
		min++;
		i++;
	}
	return (i);
}
/*
int main(void)
{
	int	min;
	int	max;
	int	*array;
	int	size;
	int	i;
	
	i = 0;
	min = 5;
	max = 10;
	size = ft_ultimate_range(&array, min, max);
	printf("size = %d\n", size);
	while(i < size)
	{
		printf("%d, ", array[i]);
		i++;
	}
}
*/
