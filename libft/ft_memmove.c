/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 16:27:41 by ridias            #+#    #+#             */
/*   Updated: 2025/10/30 16:40:50 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static void	cpy_str_rev(void *dest, const void *src, size_t n, size_t code)
{
	int	t;

	if (code == 1)
	{
		t = 0;
		while (t < (int)n)
		{
			((unsigned char *)dest)[t] = ((unsigned char *)src)[t];
			t++;
		}
	}
	else if (code == 2)
	{
		if (n == 0)
			return ;
		t = n - 1;
		while (t >= 0)
		{
			((unsigned char *)dest)[t] = ((unsigned char *)src)[t];
			t--;
		}
	}
}

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	unsigned char		*d;
	const unsigned char	*s;

	d = (unsigned char *)dest;
	s = (const unsigned char *)src;
	if (d == s)
		return (dest);
	else if (d < s)
	{
		cpy_str_rev(dest, src, n, 1);
	}
	else
	{
		cpy_str_rev(dest, src, n, 2);
	}
	return (dest);
}
