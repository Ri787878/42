/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 15:59:03 by ridias            #+#    #+#             */
/*   Updated: 2025/10/30 16:14:57 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	int	n;

	n = (int)ft_strlen(s) - 1;
	while (n >= 0)
	{
		if (s[n] == c)
			return ((char *)&s[n]);
		n--;
	}
	if (c == '\0')
		return ((char *)&s[n]);
	return (NULL);
}
