/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 11:06:56 by ridias            #+#    #+#             */
/*   Updated: 2025/11/11 15:33:49 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>

void	*ft_calloc(size_t number, size_t size)
{
	void	*objects;

	if (number == 0 | size == 0)
		return (malloc(1));
	if (number > (SIZE_MAX / size))
		return (NULL);
	objects = malloc(number * size);
	if (!objects)
		return (NULL);
	ft_bzero(objects, number * size);
	return (objects);
}

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

char	*read_and_append(int fd, char *overflow)
{
	char	*buffer;
	ssize_t	bytes_read;

	if (!overflow)
		res = ft_calloc(1, 1);
	buffer = ft_calloc(BUFFER_SIZE + 1, sizeof(char));
	bytes_read = 1;
	while (bytes_read > 0)
	{
		bytes_read = read(fd, buffer, BUFFER_SIZE);
		if (byte_read == -1)
		{
			free(buffer);
			return (NULL);
		}
		buffer[bytes_read] = '\0';
		res = ft_free(res, buffer);
		
	}
	return (read_str)
}

char	*get_next_line(int fd)
{
	static char	*buffer;

	if (BUFFER_SIZE <= 0 || fd < 0 || read(fd, 0, 0) < 0)
		return (NULL);
	buffer = read_and_append(fd, buffer);
	if (!buffer)
		return (NULL);
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
