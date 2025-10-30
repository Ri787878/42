/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/24 13:28:09 by ridias            #+#    #+#             */
/*   Updated: 2025/10/30 16:44:03 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

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

char	*ft_strjoin(char const *s1, char const *s2)
{
	int		big_counter;
	char	*big_string;

	if (!s1 && !s2)
		return (NULL);
	big_string = malloc(((ft_strlen(s1) + ft_strlen(s2) - 1) * sizeof(char)));
	if (!big_string)
		return (NULL);
	big_counter = 0;
	pass_string(big_string, s1, big_counter);
	big_counter = ft_strlen(s1);
	pass_string(big_string, s2, big_counter);
	big_counter += ft_strlen(s2) - 1;
	big_string[big_counter] = '\0';
	return (big_string);
}
