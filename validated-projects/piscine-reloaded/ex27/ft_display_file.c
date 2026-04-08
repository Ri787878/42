/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_display_file.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 16:39:43 by ridias            #+#    #+#             */
/*   Updated: 2025/10/16 18:38:41 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int	error_check(int argc)
{
	if (argc <= 1)
	{
		write(1, "File name missing.\n", 19);
		return (0);
	}
	if (argc > 2)
	{
		write(1, "Too many arguments.\n", 21);
		return (0);
	}
	return (1);
}

int	main(int argc, char **argv)
{
	int		file;
	char	buffer[1024];
	int		reads;

	if (error_check(argc) == 0)
		return (0);
	file = open(argv[1], O_RDONLY);
	if (file == -1)
	{
		write(1, "Cannot read file.\n", 19);
		return (0);
	}
	reads = read(file, buffer, 1024);
	while (reads > 0)
	{
		write(1, buffer, reads);
		reads = read(file, buffer, 1024);
	}
	close(file);
	return (0);
}
