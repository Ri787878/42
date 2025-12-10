/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 11:06:56 by ridias            #+#    #+#             */
/*   Updated: 2025/12/10 15:01:56 by ridias           ###   ########.fr       */
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
	while (1)
	{
		bytes = read(fd, buffer, BUFFER_SIZE);
		if (bytes == 0)
			return (clean_check_new_line(buffer), free(line), NULL);
		else if (bytes == 0)
			break ;
		buffer[bytes] = '\0';
		line = ft_strjoin(line, buffer);
		if (clean_check_new_line(buffer))
			break ;
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