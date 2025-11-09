/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 11:06:56 by ridias            #+#    #+#             */
/*   Updated: 2025/11/09 17:35:08 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>

static char	*pass_string(char *big_string, char const *string, int big_counter)
{
	int	t;

	t = 0;
	while (string[t] != '\0')
	{
		big_string[big_counter] = string[t];
		t++;
		big_counter++;
	}
	return (big_string);
}

char	*ft_strjoin(const char *s1, const char *s2)
{
	int		big_counter;
	char	*big_string;

	if (!s1 || !s2)
		return (NULL);
	big_string = malloc(((ft_strlen(s1) + ft_strlen(s2) + 1) * sizeof(char)));
	if (!big_string)
		return (NULL);
	big_counter = 0;
	pass_string(big_string, s1, big_counter);
	big_counter = ft_strlen(s1);
	pass_string(big_string, s2, big_counter);
	big_counter += ft_strlen(s2);
	big_string[big_counter] = '\0';
	return (big_string);
}

void	print_file_line(int fd)
{
	static char	*stash = NULL;
	char		*buffer;
	char		*combined;
	char		*newline_pos;
	char		*result;
	size_t		line_len;
	ssize_t		bytes_read;

	buffer = calloc(BUFFER_SIZE + 1, sizeof(char));
	if (!buffer)
		return ;
	bytes_read = read(fd, buffer, BUFFER_SIZE);
	if (bytes_read <= 0)
	{
		free(buffer);
		return ;
	}
	combined = ft_strjoin(stash, buffer);
	free(stash);
	stash = NULL;
	newline_pos = ft_strchr(combined, '\n');
	if (newline_pos)
	{
		line_len = newline_pos - combined + 1;
		result = malloc(line_len + 1);
		if (!result)
		{
			free(buffer);
			free(combined);
			return ;
		}
		ft_strlcpy(result, combined, line_len + 1);
		stash = ft_strdup(newline_pos + 1);
	}
	else
	{
		result = ft_strdup(combined);
	}
	ft_putstr(result);
	free(result);
	free(buffer);
	free(combined);
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
*/
