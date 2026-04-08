/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/25 13:58:46 by ridias            #+#    #+#             */
/*   Updated: 2025/09/29 11:36:58 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
//#include <stdio.h>

int	*ft_range(int min, int max)
{
	int	n;
	int	size;
	int	*str;

	size = max - min;
	if (min >= max)
		return (NULL);
	str = (int *)malloc(size * sizeof(int));
	if (!(str))
		return (NULL);
	n = 0;
	while (min < max)
	{
		str[n] = min;
		min++;
		n++;
	}
	return (str);
}

/* int	main(void)
{
	int	*dest;
	int min = -50;
	int	max = 50;
	int	n = 0;

	dest = ft_range(min, max);
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