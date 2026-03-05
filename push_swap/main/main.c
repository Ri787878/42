/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/13 11:45:14 by ridias            #+#    #+#             */
/*   Updated: 2026/03/05 12:15:54 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

static	void	ps_init(t_ps_struct *ps)
{
	ps->cmds = NULL;
	ps->cmd_count = 0;
	ps->temp_node = NULL;
	ps->a = NULL;
	ps->b = NULL;
}

void	print_content(void	*content)
{
	ft_printf("%d ", *(int *)content);
}

int	check_repeat_ints(t_list *lst)
{
	int		i;
	int		j;
	int		list_size;
	t_list	*temp;

	i = 0;
	j = 0;
	temp = lst;
	while (i < list_size)
	{
		while (j < list_size)
		{
			if ()
			j++;
		}
		i++;
	}
	return (1);
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
	if (argc < 2)
		return (0);
	if (collect_tokens(argc, argv, &ps) != 0)
		return (ft_putstr_fd("Error\n", 2), 1);
	if (check_repeat_ints(ps.a))
		return (ft_lstclear(&ps.a, free), ft_putstr_fd("Error\n", 2), 1);
	if (is_sorted(ps.a))
		return (ft_lstclear(&ps.a, free), 0);
	ft_printf("\t");
	ft_lstiter(ps.a, print_content);
	ft_lstclear(&ps.a, free);
	return (0);
}
