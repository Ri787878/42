/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/23 15:14:02 by ridias            #+#    #+#             */
/*   Updated: 2026/03/03 16:37:54 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

static void	clrs(char **parts)
{
	int	k;

	if (!parts)
		return;
	k = 0;
	while (parts[k])
		free(parts[k++]);
	free(parts);
}

static int	check_digits(const char *s)
{
	int	i;

	i = 0;
	if (s[i] == '+' || s[i] == '-')
		i++;
	if (s[i] < '0' || s[i] > '9')
		return (0);
	while (s[i])
	{
		if (s[i] < '0' || s[i] > '9')
			return (0);
		i++;
	}
	return (1);
}

int	parse_int_strict(const char *s, int *out)
{
	int		i;
	int		sign;
	long	result;

	if (s == NULL || *s == '\0' || out == NULL || check_digits(s) == 0)
		return (0);
	i = 0;
	sign = 1;
	result = 0;
	if (s[i] == '+' || s[i] == '-')
	{
		if (s[i] == '-')
			sign = -1;
		i++;
	}
	while (s[i] >= '0' && s[i] <= '9')
	{
		result = result * 10 + (s[i] - '0');
		i++;
	}
	*out = (int)(result * sign);
	return (1);
}
int	create_int_node(char **parts, t_ps_struct *ps)
{
	int	j;
	int	*p;
	int	value;

	j = 0;
	while (parts[j])
	{
		if (!parse_int_strict(parts[j], &value))
			return (-1);
		p = (int *)malloc(sizeof(int));
		if (!p)
			return (-1);
		*p = value;
		ps->temp_node = ft_lstnew(p);
		if (!ps->temp_node)
			return (free(p), -1);
		ft_lstadd_back(&ps->a, ps->temp_node);
		j++;
	}
	return (1);
}

int	collect_tokens(int argc, char **argv, t_ps_struct *ps)
{
	char	**parts;
	int	i;
	int	res;

	i = 1;
	while (i < argc)
	{
		parts = ft_split(argv[i], ' ');
		if (!parts)
			return (ft_lstclear(&ps->a, free), -1);
		res = create_int_node(parts, ps);
		if (res == -1)
			return (clrs(parts), ft_lstclear(&ps->a, free), -1);
		clrs(parts);
		i++;
	}
	return (0);
}
