/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <rmano-cl@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/16 13:45:22 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/10/16 13:55:43 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_memcmp(const void *w1, const void *w2, size_t count)
{
	size_t	i;

	i = 0;
	while (i < count)
	{
		if (((unsigned char *)w1)[i] != ((unsigned char *)w2)[i])
			return (((unsigned char *)w1)[i] - ((unsigned char *)w2)[i]);
		i++;
	}
	return (((unsigned char *)w1)[i] - ((unsigned char *)w2)[i]);
}
