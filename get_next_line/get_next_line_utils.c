/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 11:06:53 by ridias            #+#    #+#             */
/*   Updated: 2026/01/05 14:30:01 by ridias           ###   ########.fr       */
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

char	*ft_strjoin_nl(char *s1, char *s2)
{
	char	*big_string;
	size_t	i;
	size_t	x;

	if (!s2 || s2[0] == '\0')
		return (s1);
	big_string = malloc(((ft_strlen(s1) + ft_strlen(s2) + 1) * sizeof(char)));
	if (!big_string)
		return (free(s1), NULL);
	i = 0;
	x = 0;
	while (s1 && s1[x])
		big_string[i++] = s1[x++];
	x = 0;
	while (s2[x] && s2[x] != '\n')
		big_string[i++] = s2[x++];
	if (s2[x] == '\n')
		big_string[i++] = '\n';
	big_string[i] = '\0';
	free(s1);
	return (big_string);
}

int	fill_buffer(int fd, char *buffer)
{
	int	bytes_read;

	if (buffer[0] != '\0')
		return (1);
	bytes_read = read(fd, buffer, BUFFER_SIZE);
	if (bytes_read <= 0)
		return (0);
	buffer[bytes_read] = '\0';
	return (1);
}

int	ft_is_nl(char *buffer)
{
	size_t	i;
	size_t	x;
	int		found;

	i = 0;
	x = 0;
	found = 0;
	while (buffer[i])
	{
		if (found)
		{
			buffer[x] = buffer[i];
			x++;
		}
		if (buffer[i] == '\n')
			found = 1;
		buffer[i] = '\0';
		i++;
	}
	buffer[x] = '\0';
	return (found);
}
