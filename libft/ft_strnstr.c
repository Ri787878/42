/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 18:30:25 by ridias            #+#    #+#             */
/*   Updated: 2025/10/30 17:17:16 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	sub_string_check(char *str, char *needle, size_t len, int index)
{
	int	needle_size;

	needle_size = ft_strlen(needle);
	if (index + needle_size > (int)len)
		return (-1);
	while (*str == *needle && needle_size > 0)
	{
		if (*needle == '\0')
			return (1);
		if (*str == '\0')
			return (-1);
		str++;
		needle++;
		needle_size++;
	}
	if (*needle == '\0')
		return (1);
	else
		return (-1);
}

char	*ft_strnstr(const char *str, const char *to_find, size_t len)
{
	size_t	t;
	char	*haystack;
	char	*needle;

	t = 0;
	haystack = (char *)str;
	needle = (char *)to_find;
	while (haystack[t] != '\0' && t < len)
	{
		if (sub_string_check(&haystack[t], needle, len, t) == 1)
			return (&haystack[t]);
		t++;
	}
	return (NULL);
}
