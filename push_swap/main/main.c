/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/13 11:45:14 by ridias            #+#    #+#             */
/*   Updated: 2026/03/05 13:02:24 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

static	void	ps_init(t_ps_struct *ps)
{
	ps->cmds = NULL;
	ps->ac = 0;
	ps->av = NULL;
	ps->cmd_count = 0;
	ps->temp_node = NULL;
	ps->a = NULL;
	ps->b = NULL;
}

void	print_content(void	*content)
{
	ft_printf("%d ", *(int *)content);
}

int	is_sorted(t_list *lst)
{
	(void)lst;
	return (0);
}

int	main(int argc, char **argv)
{
	t_ps_struct	ps;

	ps_init(&ps);
	ps.ac = argc;
	ps.av = argv;
	if (ps->ac < 2 || !ps->av[1][0])
		return (1);
	if (!ft_filter(ps))
		return (ft_putstr_fd("Error\n", 2), 1);
	if (is_sorted(ps.a))
		return (ft_lstclear(&ps.a, free), 0);
	ft_printf("\t");
	ft_lstiter(ps.a, print_content);
	ft_lstclear(&ps.a, free);
	return (0);
}
