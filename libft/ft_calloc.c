/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 19:28:53 by ridias            #+#    #+#             */
/*   Updated: 2025/10/30 17:01:30 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t number, size_t size)
{
	void	*objects;

	if (number == 0 | size == 0)
		return (malloc(1));
	if (number > (SIZE_MAX / size))
		return (NULL);
	objects = malloc(number * size);
	if (!objects)
		return (NULL);
	ft_bzero(objects, number * size);
	return (objects);
}
