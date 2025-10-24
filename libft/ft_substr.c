/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/24 13:07:16 by ridias            #+#    #+#             */
/*   Updated: 2025/10/24 14:04:31 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	int		t;
	int		sub_string_size;
	char	*sub_string;

	if (!s || len <= 0 || start >= len)
		return (NULL);
	t = 0;
	sub_string_size = len - start;
	sub_string = malloc(sub_string_size * sizeof(char));
	if (!sub_string)
		return (NULL);
	while (t + (int)start < (int)len)
	{
		sub_string[t] = (char)s[t + (int)start];
		t++;
	}
	sub_string[t] = '\0';
	return (sub_string);
}
