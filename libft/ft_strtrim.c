/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/24 14:29:32 by ridias            #+#    #+#             */
/*   Updated: 2025/10/30 16:44:40 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	int		t;
	int		start;
	int		end;
	int		trimed_leng;
	char	*trimed_string;

	if (!s1 || !set)
		return (NULL);
	start = 0;
	end = ft_strlen(s1) - 1;
	while (ft_strchr(set, s1[start]))
		start++;
	while (ft_strchr(set, s1[end]))
		end--;
	trimed_leng = end - start;
	trimed_string = malloc(trimed_leng * sizeof(char));
	t = 0;
	while (start <= end)
	{
		trimed_string[t] = s1[start];
		t++;
		start++;
	}
	return (trimed_string);
}
