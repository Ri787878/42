/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/23 15:14:02 by ridias            #+#    #+#             */
/*   Updated: 2026/03/16 14:49:27 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

static void	clrs(char **parts)
{
	int	k;

	if (!parts)
		return ;
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

int	is_duplicate(t_list *stack, int num)
{
	if (!stack)
		return (0);
	while (stack)
	{
		if (*(int *)stack->content == num)
			return (1);
		stack = stack->next;
	}
	return (0);
}

static int	parse_one(t_ps_struct *ps, char **parts, int i)
{
	long	res;
	t_num	*num;

	if (!check_digits(parts[i]))
		return (0);
	res = ft_atol(parts[i]);
	if (res < -2147483648 || res > 2147483647)
		return (0);
	if (is_duplicate(ps->a, (int)res))
		return (0);
	num = (t_num *)malloc(sizeof(t_num));
	if (!num)
	{
		ft_lstclear(&ps->a, free);
		return (0);
	}
	num->value = (int)res;
	ft_lstadd_back(&ps->a, ft_lstnew(num));
	return (1);
}

int	ft_filter(t_ps_struct *ps)
{
	char	**parts;
	int		i;

	if (ps->ac == 2)
		parts = ft_split(ps->av[1], ' ');
	else
		parts = ps->av + 1;
	if (!parts)
		return (0);
	i = -1;
	while (parts[++i])
	{
		if (!parse_one(ps, parts, i))
		{
			if (ps->ac == 2)
				clrs(parts);
			return (0);
		}
	}
	if (ps->ac == 2)
		clrs(parts);
	return (1);
}
