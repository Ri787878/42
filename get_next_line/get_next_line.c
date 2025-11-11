/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 11:06:56 by ridias            #+#    #+#             */
/*   Updated: 2025/11/11 14:49:03 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	n;
	size_t	src_leng;
	size_t	dst_leng;

	n = 0;
	src_leng = ft_strlen(src);
	dst_leng = ft_strlen(dst);
	if (src == NULL)
		return (0);
	if (dst == NULL || size == 0)
		return (src_leng);
	if (dst_leng >= size)
		return (src_leng + size);
	while ((n + dst_leng < size - 1) && src[n] != '\0')
	{
		dst[dst_leng + n] = src[n];
		n++;
	}
	dst[dst_leng + n] = '\0';
	return (dst_leng + src_leng);
}

char	*extract_line(char **buffer)
{
	int		index;
	char	*overflow;

	index = find_new_line(*buffer);
	overflow = malloc((index + 2) * sizeof(char));
	if (!overflow)
		return (NULL);
	ft_strlcpy(overlow, *buffer, index + 2)
	return (overflow);
}

char	*read_and_append(int fd, char *read_str)
{
	char	*to_add;

	to_add = malloc((BUFFER_SIZE + 1) * sizeof(char));
	if (!to_add)
		return (NULL);
	read(fd, to_add, BUFFER_SIZE);
	to_add[BUFFER_SIZE + 1] = '\0';
	
	return (read_str)
}

char	*get_next_line(int fd)
{
	static char	*buffer;

	buffer = NULL;
	if (!)
		retun (NULL);
	buffer = read_and_append(fd, buffer);
	
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

/*
char	*get_next_line(int fd)
{
	size_t		bytes_read;
	char		*buffer;
	static int	t;

	buffer = calloc(count, sizeof(char));
	bytes_read = read(fd, buffer, BUFFER_SIZE);
	while (buffer[t] != '\n' || t == 42)
		t++;
	rest = &buffer[t];
	return ()
}









void	print_file_line(int fd)
{
	int			t;
	size_t		bytes_read;
	static char	*stash;
	char		*buffer;
	char		*result;

	t = 0;
	stash = NULL;
	buffer = calloc(BUFFER_SIZE + 1, sizeof(char));
	if (!buffer)
		return ;
	bytes_read = read(fd, buffer, BUFFER_SIZE);
	if (bytes_read <= 0)
	{
		free(buffer);
		return ;
	}
	t = find_chr(buffer, '\n') + 1;
	if (t == -42)
	{
		printf("\"%s\"\n", buffer);
		write(1, "Error on find_chr\n", 19);
		return ;
	}
	else if (t >= 0)
	{
		result = calloc(t + 1, sizeof(char));
		if (!buffer)
		{
			free(buffer);
			return ;
		}
		ft_strlcpy(overflow, buffer, t);
		ft_putstr(overflow);
	}
	free(overflow);
	free(buffer);
}




char	*get_next_line(int fd)
{
	static char	*buffer;
	char		*result;

	t = 0;
	if (!buffer)
		buffer = calloc(BUFFER_SIZE + 1, sizeof(char));
	if (fd < 0 || BUFFER_SIZE == 0 || read(fd, 0, 0) < 0)
		return (NULL);
	buffer = read_remainder(fd, buffer);
	if (bytes_read <= 0)
	{
		free(buffer);
		return ;
	}
	t = find_chr(buffer, '\n') + 1;
	if (t == -42)
	{
		printf("\"%s\"\n", buffer);
		write(1, "Error -42 on find_chr\n", 23);
		return (NULL);
	}/*
char	*get_next_line(int fd)
{
	size_t		bytes_read;
	char		*buffer;
	static int	t;

	buffer = calloc(count, sizeof(char));
	bytes_read = read(fd, buffer, BUFFER_SIZE);
	while (buffer[t] != '\n' || t == 42)
		t++;
	rest = &buffer[t];
	return ()
}









void	print_file_line(int fd)
{
	int			t;
	size_t		bytes_read;
	static char	*stash;
	char		*buffer;
	char		*result;

	t = 0;
	stash = NULL;
	buffer = calloc(BUFFER_SIZE + 1, sizeof(char));
	if (!buffer)
		return ;
	bytes_read = read(fd, buffer, BUFFER_SIZE);
	if (bytes_read <= 0)
	{
		free(buffer);
		return ;
	}
	t = find_chr(buffer, '\n') + 1;
	if (t == -42)
	{
		printf("\"%s\"\n", buffer);
		write(1, "Error on find_chr\n", 19);
		return ;
	}
	else if (t >= 0)
	{
		result = calloc(t + 1, sizeof(char));
		if (!buffer)
		{
			free(buffer);
			return ;
		}
		ft_strlcpy(overflow, buffer, t);
		ft_putstr(overflow);
	}
	free(overflow);
	free(buffer);
}




char	*get_next_line(int fd)
{
	static char	*buffer;
	char		*result;

	t = 0;
	if (!buffer)
		buffer = calloc(BUFFER_SIZE + 1, sizeof(char));
	if (fd < 0 || BUFFER_SIZE == 0 || read(fd, 0, 0) < 0)
		return (NULL)
	else if (t >= 0)
	{
		result = calloc(t + 1, sizeof(char));
		if (!buffer)
		{
			free(buffer);
			return ;
		}
		ft_strlcpy(result, buffer, t);
		buffer = &buffer[t];
		return (result);
	}
	free(result);
	free(buffer);
}


*/