/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 11:06:56 by ridias            #+#    #+#             */
/*   Updated: 2025/11/16 14:28:39 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>

static char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	size_t	t;
	char	*sub_string;

	if (!s)
		return (NULL);
	if (start > ft_strlen(s))
		return (ft_strdup(""));
	if ((ft_strlen(s) - start) < len)
		len = ft_strlen(s) - start;
	t = 0;
	sub_string = malloc((len + 1) * sizeof(char));
	if (!sub_string)
		return (NULL);
	while (t < len && start < ft_strlen(s))
	{
		sub_string[t] = s[t + (int)start];
		t++;
	}
	sub_string[t] = '\0';
	return (sub_string);
}

void	ft_bzero(void *s, size_t n)
{
	size_t			t;
	unsigned char	*str;

	str = (unsigned char *)s;
	t = 0;
	while (t < n)
	{
		str[t] = '\0';
		t++;
	}
	return ;
}

void	*ft_calloc(size_t number, size_t size)
{
	void	*objects;

	if (number == 0 || size == 0)
		return (malloc(1));
	if (number > (SIZE_MAX / size))
		return (NULL);
	objects = malloc(number * size);
	if (!objects)
		return (NULL);
	ft_bzero(objects, number * size);
	return (objects);
}

char	*read_and_append(int fd, char *buffer)
{
	char	*temp_buffer;
	ssize_t	bytes_read;
	char	*new_buffer;

	if (!buffer)
		buffer = ft_calloc(1, 1);
	bytes_read = 1;
	while (bytes_read > 0)
	{
		temp_buffer = ft_calloc(BUFFER_SIZE + 1, sizeof(char));
		bytes_read = read(fd, temp_buffer, BUFFER_SIZE);
		if (bytes_read == -1)
		{
			free(temp_buffer);
			free(buffer);
			return (NULL);
		}
		temp_buffer[bytes_read] = '\0';
		new_buffer = ft_strjoin(buffer, temp_buffer);
		free(temp_buffer);
		free(buffer);
		buffer = new_buffer;
		if (find_new_line(buffer) != -1)
			return (buffer);
	}
	return (buffer);
}

char	*get_next_line(int fd)
{
	static char	*buffer;
	char		*line;
	char		*temp;
	int			index;

	if (BUFFER_SIZE <= 0 || fd < 0)
		return (NULL);
	if (buffer && find_new_line(buffer) != -1)
	{
		index = find_new_line(buffer) + 1;
		line = ft_substr(buffer, 0, index);
		temp = ft_substr(buffer, index, ft_strlen(buffer));
		free(buffer);
		buffer = temp;
	}
	else
	{
		if (read(fd, 0, 0) < 0)
		{
			free(buffer);
			buffer = NULL;
			return (NULL);
		}
		buffer = read_and_append(fd, buffer);
		if (!buffer)
			return (NULL);
		if (buffer[0] == '\0')
		{
			free(buffer);
			buffer = NULL;
			return (NULL);
		}
		index = find_new_line(buffer) + 1;
		if (index - 1 != -1)
		{
			line = ft_substr(buffer, 0, index);
			if (!line)
				return (NULL);
			temp = ft_substr(buffer, index, ft_strlen(buffer));
			free(buffer);
			buffer = temp;
		}
		else
		{
			line = buffer;
			free(buffer);
			buffer = NULL;
		}
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
