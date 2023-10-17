/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <rmano-cl@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/16 13:44:58 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/10/16 13:50:41 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t num, size_t size )
{
	void	*ptr;

	ptr = malloc(num * size);
	if (ptr)
		ft_memset(ptr, 0, num * size);
	return (ptr);
}
