/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/08 11:04:21 by ridias            #+#    #+#             */
/*   Updated: 2026/01/08 11:57:57 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*get_next_line(int fd)
{
	static char	buffer[BUFFER_SIZE + 1];
	char		*line;
	int			bytes;

	if (BUFFER_SIZE < 1 || fd < 0)
		return (NULL);
	line = NULL;
	while (1)
	{
		if (*buffer == 0)
		{
			bytes = read(fd, buffer, BUFFER_SIZE);
			if (bytes < 0)
				return (clean_check_nl(buffer), free(line), NULL);
			else if (bytes == 0)
				break ;
			buffer[bytes] = '\0';
		}
		line = ft_strjoin(line, buffer);
		if (clean_check_nl(buffer))
			break ;
	}
	return (line);
}
/* 
#include <stdio.h>

int	main(void)
{
	int		fd;
	char	*line;

	fd = open("test1.txt", O_RDONLY);
	while (1)
	{
		line = get_next_line(fd);
		if (!line)
		{
			free(line);
			break ;
		}
		printf("%s", line);
		free(line);
	}
	close(fd);
	return (0);
}
 */