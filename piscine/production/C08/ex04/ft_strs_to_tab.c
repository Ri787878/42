/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strs_to_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/29 15:55:16 by ridias            #+#    #+#             */
/*   Updated: 2025/10/01 12:01:25 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_stock_str.h"

#include <stdlib.h>
#include <unistd.h>

int	ft_strlen(char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
	{
		n++;
	}
	return (n);
}

char	*ft_strdup(char *src)
{
	int		n;
	char	*str;

	n = 0;
	str = malloc(sizeof(char) * (ft_strlen(src) + 1));
	if (str == NULL)
		return (NULL);
	while (src[n])
	{
		str[n] = src[n];
		n++;
	}
	str[n] = '\0';
	return (str);
}

struct s_stock_str	*ft_strs_to_tab(int ac, char **av)
{
	struct s_stock_str	*tab;
	int					i;

	tab = (t_stock_str *) malloc(sizeof(t_stock_str) * (ac + 1));
	if (tab == NULL)
		return (NULL);
	i = 0;
	while (i < ac)
	{
		if (av[i] == NULL)
			return (NULL);
		tab[i].size = ft_strlen(av[i]);
		tab[i].str = ft_strdup(av[i]);
		tab[i].copy = ft_strdup(av[i]);
		if (tab[i].str == NULL || tab[i].copy == NULL)
			return (NULL);
		i++;
	}
	tab[i].str = NULL;
	return (tab);
}

/* int main (void)
{
	char	*array[] = {"Maria", "Adriana", "VANESSAAA!!"};
	int		size;

	size = 3;
	
	t_stock_str **container = NULL;
	*container = ft_strs_to_tab(size, array);
	while (*container)
	{
		ft_show_tab(*container);
		container++;
	}
	return (0);
} */