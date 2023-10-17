/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <rmano-cl@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/09 15:03:30 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/10/16 14:02:36 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	size_t		i;
	char		*dest_temp;
	const char	*src_temp;

	dest_temp = (char *)dest;
	src_temp = (const char *)src;
	i = 0;
	if (dest_temp < src_temp)
	{
		while (i < n)
		{
			dest_temp[i] = src_temp[i];
			i++;
		}
	}
	else
	{
		while (n > 0)
		{
			dest_temp[n - 1] = src_temp[n - 1];
			n--;
		}
	}
	return (dest);
}
