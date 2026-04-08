/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 14:35:48 by ridias            #+#    #+#             */
/*   Updated: 2025/11/04 11:04:12 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	unsigned char	*p_s1;
	unsigned char	*p_s2;
	size_t			i;

	p_s1 = (unsigned char *)s1;
	p_s2 = (unsigned char *)s2;
	i = 0;
	if (n == 0)
		return (0);
	while (i < n && p_s1[i] == p_s2[i])
		i++;
	if (i < n && p_s1[i] < p_s2[i])
		return (-p_s2[i]);
	if (i < n && p_s1[i] > p_s2[i])
		return (p_s1[i]);
	return (0);
}
