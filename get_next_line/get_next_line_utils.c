/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 11:06:53 by ridias            #+#    #+#             */
/*   Updated: 2025/11/16 16:48:16 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

size_t	ft_strlen(const char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
	{
		n++;
	}
	return (n);
}

void	ft_bzero(void *s, size_t n)
{
	size_t			t;
	unsigned char	*str;

	str = (unsigned char *)s;
	t = 0;
	while (t < n)
	{
		str[t] = '\0';
		t++;
	}
	return ;
}

void	*ft_calloc(size_t number, size_t size)
{
	void	*objects;

	if (number == 0 || size == 0)
		return (malloc(1));
	if (number > (SIZE_MAX / size))
		return (NULL);
	objects = malloc(number * size);
	if (!objects)
		return (NULL);
	ft_bzero(objects, number * size);
	return (objects);
}
