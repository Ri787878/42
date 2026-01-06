/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 11:06:56 by ridias            #+#    #+#             */
/*   Updated: 2026/01/06 16:33:33 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

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
int main(void)
{
	int fd = open("ink.txt", O_RDONLY);
	char *line;
	while ((line = get_next_line(fd)) != NULL)
	{
		printf("%s", line);
		free(line);
	}
	free(line);
	close(fd);
	return 0;
	printf("\n");
}*/