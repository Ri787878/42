/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate_complex.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/12 13:59:59 by ridias            #+#    #+#             */
/*   Updated: 2026/03/16 15:16:31 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

static int	reverse_rotate_a(t_ps_struct *ps)
{
	t_list	*prev;
	t_list	*last;

	if (!ps || !ps->a || !ps->a->next)
		return (0);
	prev = NULL;
	last = ps->a;
	while (last->next)
	{
		prev = last;
		last = last->next;
	}
	prev->next = NULL;
	last->next = ps->a;
	ps->a = last;
	return (1);
}

static int	reverse_rotate_b(t_ps_struct *ps)
{
	t_list	*prev;
	t_list	*last;

	if (!ps || !ps->b || !ps->b->next)
		return (0);
	prev = NULL;
	last = ps->b;
	while (last->next)
	{
		prev = last;
		last = last->next;
	}
	prev->next = NULL;
	last->next = ps->b;
	ps->b = last;
	return (1);
}

void	rra(t_ps_struct *ps)
{
	if (reverse_rotate_a(ps))
		ft_printf("rra\n");
}

void	rrb(t_ps_struct *ps)
{
	if (reverse_rotate_b(ps))
		ft_printf("rrb\n");
}

void	rrr(t_ps_struct *ps)
{
	if (!ps || !ps->a || !ps->a->next || !ps->b || !ps->b->next)
		return ;
	reverse_rotate_a(ps);
	reverse_rotate_b(ps);
	ft_printf("rrr\n");
}
