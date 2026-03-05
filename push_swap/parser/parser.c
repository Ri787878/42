/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/23 15:14:02 by ridias            #+#    #+#             */
/*   Updated: 2026/03/05 13:09:33 by ridias           ###   ########.fr       */
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
	int	i;
	int *p;

	if (ps->ac == 2)
		parts = ft_split(ps->av[1], ' ');
	else
		parts = ps->av + 1; // ELABORATE ON THIS CODE
	p = (int *)malloc(sizeof(int));
	if (!p)
		return (clrs(parts), 0);
	*p = (int)res;
		i = -1;
	while (parts[++i])
	{
		if (!check_digits(parts[i]))
			return (clrs(parts), 0);
		res = ft_atoi(parts[i]);
		if (res < -2147483648 || res > 2147483647)
			return (clrs(parts), 0);
		if (is_duplicate(ps->a, (int)res))
			return (clrs(parts), 0);
		ft_lstadd_back(&ps->a, ft_lstnew((int)res));
	}
	if (ps->ac == 2)
		clrs(parts);
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
