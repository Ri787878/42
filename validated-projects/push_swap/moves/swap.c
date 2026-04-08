/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/12 14:00:03 by ridias            #+#    #+#             */
/*   Updated: 2026/03/16 15:16:49 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

static int	swap_a(t_ps_struct *ps)
{
	t_list	*first;
	t_list	*second;

	first = NULL;
	second = NULL;
	if (!ps || !ps->a || !ps->a->next)
		return (0);
	first = ps->a;
	second = first->next;
	first->next = second->next;
	second->next = first;
	ps->a = second;
	return (1);
}

static int	swap_b(t_ps_struct *ps)
{
	t_list	*first;
	t_list	*second;

	first = NULL;
	second = NULL;
	if (!ps || !ps->b || !ps->b->next)
		return (0);
	first = ps->b;
	second = first->next;
	first->next = second->next;
	second->next = first;
	ps->b = second;
	return (1);
}

void	sa(t_ps_struct *ps)
{
	if (swap_a(ps))
	{
		ft_printf("sa\n");
		return ;
	}
}

void	sb(t_ps_struct *ps)
{
	if (swap_b(ps))
	{
		ft_printf("sb\n");
		return ;
	}
}

void	ss(t_ps_struct *ps)
{
	int	swaped_a;
	int	swaped_b;

	swaped_a = swap_a(ps);
	swaped_b = swap_b(ps);
	if (swaped_a && swaped_b)
		ft_printf("ss\n");
}
