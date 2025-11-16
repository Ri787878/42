/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 11:06:56 by ridias            #+#    #+#             */
/*   Updated: 2025/11/16 16:50:40 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>

char	*read_line(int fd, char *buffer)
{
	char	*new_buffer;
	int		index;

	new_buffer = ft_calloc((BUFFER_SIZE + 1), sizeof(char));
	if (!new_buffer)
		return (NULL);
	index = 1;
	while (!(find_new_line(buffer)) && index != 0)
	{
		index = read(fd, new_buffer, BUFFER_SIZE);
		if (index < 0)
		{
			free(new_buffer);
			free(buffer);
			return (NULL);
		}
		new_buffer[index] = 0;
		buffer = ft_strjoin(buffer, new_buffer);
	}
	free(new_buffer);
	return (buffer);
}

char	*get_line(char *buffer)
{
	int		i;
	char	*line;

	i = 0;
	if (buffer[0] == '\0')
		return (NULL);
	while (buffer[i] && (buffer[i] != '\n'))
		i++;
	line = ft_calloc(i + 2, sizeof(char));
	if (!line)
		return (NULL);
	i = 0;
	while (buffer[i] && buffer[i] != '\n')
		line[i++] = buffer[i++];
	if (buffer[i] == '\n')
	{
		line[i] = buffer[i];
		i++;
	}
	line[i] = '\0';
	return (line);
}

char	*get_overflow(char	*buffer)
{
	int		i;
	int		overflow_index;
	char	*overflow;

	i = 0;
	while (buffer[i] && buffer[i] != '\n')
		i++;
	if (!buffer[i])
	{
		free(buffer);
		return (NULL);
	}
	overflow = malloc((ft_strlen(buffer) - i + 1) * sizeof(char));
	if (!overflow)
	{
		free(overflow);
		return (NULL);
	}
	i += 1;
	overflow_index = 0;
	while (buffer[i] && buffer[i] != '\n')
		overflow[overflow_index++] = buffer[i++];
	overflow[overflow_index] = '\0';
	free(buffer);
	return (overflow);
}

char	*get_next_line(int fd)
{
	static char	*buffer;
	char		*line;

	if (BUFFER_SIZE <= 0 || fd < 0)
		return (NULL);
	buffer = read_line(fd, buffer);
	if (!buffer)
		return (NULL);
	line = get_line(buffer);
	buffer = get_overflow(buffer);
	return (line);
}
/*
int	main(void)
{
	int	fd;
	int	size;

	fd = open("ink.txt", O_RDONLY);
	if (fd < 0)
	{
		ft_putstr("Error in fd assining.\n");
		return (-1);
	}
	print_file_line(fd);

	return (0);
}
*/
