/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 18:30:25 by ridias            #+#    #+#             */
/*   Updated: 2025/11/04 11:07:31 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	sub_str_check(const char *str, char *needle, size_t len, int index)
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
	char	*needle;

	if (*to_find == '\0')
		return ((char *)str);
	t = 0;
	needle = (char *)to_find;
	while (str[t] != '\0' && t < len)
	{
		if (sub_str_check(&str[t], needle, len, t) == 1)
			return ((char *)&str[t]);
		t++;
	}
	return (NULL);
}
