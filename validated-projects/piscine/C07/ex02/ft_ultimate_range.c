/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_range.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/25 15:25:59 by ridias            #+#    #+#             */
/*   Updated: 2025/09/29 10:44:34 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

int	ft_ultimate_range(int **range, int min, int max)
{
	int	n;
	int	size;
	int	*result;

	if (min >= max)
	{
		return (0);
	}
	size = max - min;
	result = (int *)malloc(size * sizeof(int));
	if (!result)
	{
		return (-1);
	}
	n = 0;
	while (min < max)
	{
		result[n] = min;
		min++;
		n++;
	}
	*range = result;
	return (n);
}

/* int	main(void)
{
	int	*dest;
	int min = -50;
	int	max = 50;
	int	n = 0;
	int	leng = 0;

	leng = ft_ultimate_range(&dest, min, max);
	while (n < max - min)
	{
		printf("dest[%d] = %d", n, dest[n]);
		if (n != max - min - 1 && n % 7 != 0)
			printf(",\t");
		if (n % 7 == 0)
			printf("\n\n");
		n++;
	}
	printf("\n");

	return (0);
} */