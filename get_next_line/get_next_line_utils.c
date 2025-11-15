/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 11:06:53 by ridias            #+#    #+#             */
/*   Updated: 2025/11/15 22:33:55 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

size_t	ft_strlen(const char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
	{
		n++;
	}
	return (n);
}

int	find_new_line(const char *s)
{
	size_t	t;

	t = 0;
	while (s[t] != '\0')
	{
		if ((unsigned char)s[t] == '\n')
			return (t);
		t++;
	}
	return (-1);
}

char	*ft_strdup(const char *src)
{
	int		n;
	char	*str;

	n = 0;
	str = (char *)malloc((ft_strlen(src) + 1) * sizeof(char));
	if (!str)
		return (NULL);
	while (src[n])
	{
		str[n] = src[n];
		n++;
	}
	str[n] = '\0';
	return (str);
}

static char	*pass_string(char *big_string, char const *string, int big_counter)
{
	int	t;

	t = 0;
	while (string[t] != '\0')
	{
		big_string[big_counter] = string[t];
		t++;
		big_counter++;
	}
	return (big_string);
}

char	*ft_strjoin(const char *s1, const char *s2)
{
	int		big_counter;
	char	*big_string;

	if (!s1 || !s2)
		return (NULL);
	big_string = malloc(((ft_strlen(s1) + ft_strlen(s2) + 1) * sizeof(char)));
	if (!big_string)
		return (NULL);
	big_counter = 0;
	pass_string(big_string, s1, big_counter);
	big_counter = ft_strlen(s1);
	pass_string(big_string, s2, big_counter);
	big_counter += ft_strlen(s2);
	big_string[big_counter] = '\0';
	return (big_string);
}
