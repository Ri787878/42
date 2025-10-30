/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 14:35:15 by ridias            #+#    #+#             */
/*   Updated: 2025/10/30 15:53:27 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	n;
	size_t	src_leng;
	size_t	dst_leng;

	n = 0;
	src_leng = ft_strlen(src);
	dst_leng = ft_strlen(dst);
	if (src == NULL)
		return (0);
	if (dst == NULL || size == 0)
		return (src_leng);
	if (dst_leng >= size)
		return (src_leng + size);
	while ((n + dst_leng < size - 1) && src[n] != '\0')
	{
		dst[dst_leng + n] = src[n];
		n++;
	}
	dst[dst_leng + n] = '\0';
	return (dst_leng + src_leng);
}
