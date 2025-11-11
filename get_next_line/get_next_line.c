/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 11:06:56 by ridias            #+#    #+#             */
/*   Updated: 2025/11/11 15:22:27 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>

char	*extract_line(char **buffer)
{
	int		index;
	char	*overflow;

	index = find_new_line(*buffer);
	overflow = malloc((index + 2) * sizeof(char));
	if (!overflow)
		return (NULL);
	ft_strlcpy(overflow, *buffer, index + 2);
	return (overflow);
}

char	*read_and_append(int fd, char *buffer)
{
	char	*to_add;
	char	*buffer
	ssize_t	bytes_read;

	to_add = malloc((BUFFER_SIZE + 1) * sizeof(char));
	if (!to_add)
		return (NULL);
	bytes_read = read(fd, to_add, BUFFER_SIZE);
	to_add[bytes_read] = '\0';
	ft_strjoin()
	return (read_str)
}

char	*get_next_line(int fd)
{
	static char	*buffer;

	if (BUFFER_SIZE <= 0 || fd < 0)
	{
		if (buffer)
		{
			free(buffer);
			buffer = NULL;
		}
		return (NULL);
	}
	buffer = read_and_append(fd, buffer);
	return (buffer);
}

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
