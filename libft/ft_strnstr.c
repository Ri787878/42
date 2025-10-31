/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 18:30:25 by ridias            #+#    #+#             */
/*   Updated: 2025/10/31 14:52:50 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	sub_string_check(char *str, char *needle, size_t len, int index)
{
	size_t	t;

	t = 0;
	while (needle[t] && ((size_t)index + t) < len)
	{
		if (str[t] != needle[t])
			return (-1);
		t++;
	}
	if (needle[t] == '\0')
		return (1);
	return (-1);
}

char	*ft_strnstr(const char *str, const char *to_find, size_t len)
{
	size_t	t;
	char	*haystack;
	char	*needle;

	if (*to_find == '\0')
		return ((char *)str);
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
