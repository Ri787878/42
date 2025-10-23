/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 16:40:06 by ridias            #+#    #+#             */
/*   Updated: 2025/10/21 16:55:57 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>
#include <stdio.h>

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	const unsigned char	*p_s1;
	const unsigned char	*p_s2;
	int					i;

	p_s1 = (const unsigned char *)s1;
	p_s2 = (const unsigned char *)s2;
	i = 0;
	if ((int)n == 0)
		return (0);
	while (i < (int)n && p_s1[i] == p_s2[i])
		i++;
	if (i < (int)n && p_s1[i] < p_s2[i])
		return (-p_s2[i]);
	if (i < (int)n && p_s1[i] > p_s2[i])
		return (p_s1[i]);
	return (0);
}
