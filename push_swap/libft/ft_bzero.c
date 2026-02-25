/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 16:21:34 by ridias            #+#    #+#             */
/*   Updated: 2025/10/30 17:17:35 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

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
