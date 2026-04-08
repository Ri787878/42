/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 13:12:23 by ridias            #+#    #+#             */
/*   Updated: 2025/10/16 13:36:17 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	*ft_range(int min, int max)
{
	int		n;
	int		size;
	int		*str;

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
