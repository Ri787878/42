/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 11:06:56 by ridias            #+#    #+#             */
/*   Updated: 2026/01/05 14:24:49 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>

char	*get_next_line(int fd)
{
	static char	buffer[BUFFER_SIZE + 1];
	char		*line;
	int			bytes;

	if (BUFFER_SIZE <= 0 || fd < 0)
		return (NULL);
	line = NULL;
	bytes = 0;
	while (!bytes && fill_buffer(fd, buffer))
	{
		line = ft_strjoin_nl(line, buffer);
		if (!line)
			return (free(line), NULL);
		bytes = ft_is_nl(buffer);
	}
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
