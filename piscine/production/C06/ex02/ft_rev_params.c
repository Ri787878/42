/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_params.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/23 18:06:55 by ridias            #+#    #+#             */
/*   Updated: 2025/09/26 11:43:21 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <unistd.h>

void	ft_putchar(int c)
{
	write(1, &c, 1);
}

void	ft_putstr(char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
	{
		ft_putchar(str[n]);
		n++;
	}
}

int	main(int argc, char **argv)
{
	int	n;

	n = argc - 1;
	if (argc)
	{
		while (n > 0)
		{
			ft_putstr(argv[n]);
			ft_putchar(10);
			n--;
		}
	}
	return (0);
}
