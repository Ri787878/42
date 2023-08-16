/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/16 08:32:30 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/16 08:32:32 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>

int	*ft_range(int min, int max)
{
	int	*recheio;
	int	i;
	int	range;

	range = max - min;
	i = 0;
	recheio = malloc(sizeof(int) * (max - min));
	if (min >= max)
		return (0);
	if (!recheio)
		return (0);
	while (i < range)
	{
		recheio[i] = min;
		min++;
		i++;
	}
	return (recheio);
}

int	main(void)
{
	int	min;
	int	max;
	int	*tab;
	int	i;
	int	size;

	i = 0;
	min = 5;
	max = 10;
	size = max - min;
	tab = ft_range(min, max);
	while (i < size)
	{
		printf("%d, ", tab[i]);
		i++;
	}
}
