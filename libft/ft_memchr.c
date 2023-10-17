/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <rmano-cl@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/16 13:45:11 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/10/16 13:54:22 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *ptr, int ch, size_t count)
{
	unsigned long int	i;

	i = 0;
	while (i < count)
	{
		if (((unsigned char *)ptr)[i] == (unsigned char)ch)
			return ((void *)ptr + i);
		i++;
	}
	return (NULL);
}
