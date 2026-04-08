/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/08 11:04:29 by ridias            #+#    #+#             */
/*   Updated: 2026/01/08 11:09:31 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

int	clean_check_nl(char *buffer)
{
	size_t	i;
	size_t	j;
	size_t	found;

	i = 0;
	j = 0;
	found = 0;
	while (buffer[i])
	{
		if (found == 1)
			buffer[j++] = buffer[i];
		if (buffer[i] == '\n')
			found = 1;
		buffer[i++] = '\0';
	}
	return (found);
}

void	*ft_memcpy(void *dst, const void *src, size_t n)
{
	unsigned char	*p_src;
	unsigned char	*p_dst;
	size_t			i;

	if (!src && !dst)
		return (NULL);
	i = 0;
	p_src = (unsigned char *)src;
	p_dst = (unsigned char *)dst;
	while (i < n)
	{
		p_dst[i] = p_src[i];
		i++;
	}
	return (dst);
}

size_t	ft_strlen(const char *str)
{
	size_t	i;

	if (!str)
		return (0);
	i = 0;
	while (str[i] && str[i] != '\n')
		i++;
	if (str[i] == '\n')
		i++;
	return (i);
}

char	*ft_strjoin(char *s1, const char *s2)
{
	char	*line;
	size_t	s1_len;
	size_t	s2_len;

	s1_len = ft_strlen(s1);
	s2_len = ft_strlen(s2);
	line = malloc(s1_len + s2_len + 1);
	if (!line)
		return (NULL);
	ft_memcpy(line, s1, s1_len);
	ft_memcpy(line + s1_len, s2, s2_len);
	line[s1_len + s2_len] = '\0';
	free (s1);
	return (line);
}
