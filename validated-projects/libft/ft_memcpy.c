/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 16:23:23 by ridias            #+#    #+#             */
/*   Updated: 2025/11/03 14:34:56 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	unsigned char	*des;
	unsigned char	*sr;
	size_t			t;

	des = (unsigned char *)dest;
	sr = (unsigned char *)src;
	t = 0;
	while (t < n)
	{
		des[t] = sr[t];
		t++;
	}
	return (dest);
}
