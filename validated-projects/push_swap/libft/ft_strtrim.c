/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/24 14:29:32 by ridias            #+#    #+#             */
/*   Updated: 2025/10/31 14:55:24 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	find_in_set(const char *s, char c)
{
	int	t;

	t = 0;
	while (s[t] != '\0')
	{
		if (s[t] == c)
			return (1);
		t++;
	}
	return (0);
}

static int	index_counter(const char *set, const char *s1, int code)
{
	int	t;

	t = 0;
	if (code == 1)
	{
		while (find_in_set(set, s1[t]) == 1)
			t++;
	}
	else if (code == 2)
	{
		t = ft_strlen(s1) - 1;
		while (find_in_set(set, s1[t]) == 1)
			t--;
	}
	return (t);
}

char	*ft_strtrim(char const *s1, char const *set)
{
	int		t;
	int		start;
	int		end;
	char	*trimed_string;

	if (!s1 || !set)
		return (NULL);
	t = index_counter(set, s1, 1);
	if (s1[t] == '\0')
		return (ft_strdup(""));
	start = t;
	end = index_counter(set, s1, 2);
	t = 0;
	trimed_string = malloc(((end - start) + 2) * sizeof(char));
	if (!trimed_string)
		return (NULL);
	while (start <= end)
	{
		trimed_string[t] = s1[start];
		t++;
		start++;
	}
	trimed_string[t] = '\0';
	return (trimed_string);
}
