/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_params.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/12 17:58:15 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/12 17:58:19 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i] == s2[i] && s1[i] != '\0' && s2[i] != '\0')
	{
		i++;
	}
	return (s1[i] - s2[i]);
}

int	ft_write_params(int argc, char **argv)
{
	int	j;
	int	i;

	i = 1;
	while (i < argc)
	{
		j = 0;
		while (argv[i][j] != '\0')
		{
			write(1, &argv[i][j], 1);
			j++;
		}
		argv[i][j] = '\0';
		write(1, "\n", 1);
		i++;
	}
	return (0);
}

int	main(int argc, char **argv)
{
	char	*temp;
	int		n;

	n = 1;
	while (n < argc - 1)
	{
		if (ft_strcmp(argv[n], argv[n + 1]) > 0)
		{
			temp = argv[n];
			argv[n] = argv[n + 1];
			argv[n + 1] = temp;
			n = 1;
		}
		else
			n++;
	}
	ft_write_params(argc, argv);
	return (0);
}
//./a.out test1 test2 test3 | cat -e
/*
int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		i++;
	}
	return (i);
}

void	ft_putstr(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		write(1, &str[i], 1);
		i++;
	}
}

void	sort2(char **tab)
{
	int		i;
	char	*temp;

	i = 0;
	while (tab[i + 1] != '\0')
	{
		if (tab[i][0] > tab[i + 1][0])
		{
			temp = tab[i];
			tab[i + 1] = tab[i];
			tab[i + 1] = temp;
		}
		i++;
	}
}

void	sort(char **tab)
{
	int	size;
	int	count;
	int	i;
	int	j;

	i = 0;
	size = ft_strlen(tab);
	while (tab[i + 1] != '\0')
	{
		while (tab [i][j + 1] != '\0')
		{
			if (tab[i][j] > tab[i][j + 1])
			{
				count = tab[i][j] + count;
			}
			j++;
		}
		i++;
	}
}

*/
