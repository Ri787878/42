/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 11:06:53 by ridias            #+#    #+#             */
/*   Updated: 2025/12/10 14:58:42 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

size_t	ft_strlen(const char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
		n++;
	return (n);
}

size_t	ft_strlen_nl(const char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0' && str[n] != '\n')
		n++;
	return (n);
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

int	clean_check_new_line(char *buffer)
{
	int	i;
	int	j;
	int	nl_found;

	i = 0;
	j = 0;
	nl_found = 0;
	while (buffer[i] != '\0')
	{
		if (nl_found == 1)
			buffer[j++] = buffer[i];
		if (nl_found == 0)
			nl_found = 1;
		buffer[i] = '\0';
		i++;
	}
	return (nl_found);
}
