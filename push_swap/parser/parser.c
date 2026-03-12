/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/23 15:14:02 by ridias            #+#    #+#             */
/*   Updated: 2026/03/12 16:45:32 by ridias           ###   ########.fr       */
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

int	ft_filter(t_ps_struct *ps)
{
	char	**parts;
	long	res;
	int		i;
	int		*p;

	if (ps->ac == 2)
		parts = ft_split(ps->av[1], ' ');
	else
		parts = ps->av + 1;
	if (!parts)
		return (0);
	i = -1;
	while (parts[++i])
	{
		if (!check_digits(parts[i]))
		{
			if (ps->ac == 2)
				clrs(parts);
			return (0);
		}
		res = ft_atol(parts[i]);
		if (res < -2147483648 || res > 2147483647)
		{
			if (ps->ac == 2)
				clrs(parts);
			return (0);
		}
		if (is_duplicate(ps->a, (int)res))
		{
			if (ps->ac == 2)
				clrs(parts);
			return (0);
		}
		p = (int *)malloc(sizeof(int));
		if (!p)
		{
			if (ps->ac == 2)
				clrs(parts);
			ft_lstclear(&ps->a, free);
			return (0);
		}
		*p = (int)res;
		ft_lstadd_back(&ps->a, ft_lstnew(p));
	}
	if (ps->ac == 2)
		clrs(parts);
	return (1);
}
