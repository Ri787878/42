/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate_simple.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/12 13:59:59 by ridias            #+#    #+#             */
/*   Updated: 2026/03/12 17:57:38 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

static int	rotate_a(t_ps_struct *ps)
{
	t_list	*first;
	t_list	*last;

	if (!ps || !ps->a || !ps->a->next)
		return (0);
	first = ps->a;
	last = ps->a;
	while (last->next)
		last = last->next;
	ps->a = first->next;
	first->next = NULL;
	last->next = first;
	return (1);
}

static int	rotate_b(t_ps_struct *ps)
{
	t_list	*first;
	t_list	*last;

	if (!ps || !ps->b || !ps->b->next)
		return (0);
	first = ps->b;
	last = ps->b;
	while (last->next)
		last = last->next;
	ps->b = first->next;
	first->next = NULL;
	last->next = first;
	return (1);
}

void	ra(t_ps_struct *ps)
{
	if (rotate_a(ps))
		ft_printf("ra\n");
}

void	rb(t_ps_struct *ps)
{
	if (rotate_b(ps))
		ft_printf("rb\n");
}

void	rr(t_ps_struct *ps)
{
	int	rotated_a;
	int	rotated_b;

	rotated_a = rotate_a(ps);
	rotated_b = rotate_b(ps);
	if (rotated_a && rotated_b)
		ft_printf("rr\n");
}
