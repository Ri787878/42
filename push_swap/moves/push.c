/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/12 14:00:00 by ridias            #+#    #+#             */
/*   Updated: 2026/03/12 17:59:14 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

static int	push_a(t_ps_struct *ps)
{
	t_list	*temp;

	if (!ps || !ps->b)
		return (0);
	temp = ps->b;
	ps->b = temp->next;
	temp->next = ps->a;
	ps->a = temp;
	return (1);
}

static int	push_b(t_ps_struct *ps)
{
	t_list	*temp;

	if (!ps || !ps->a)
		return (0);
	temp = ps->a;
	ps->a = temp->next;
	temp->next = ps->b;
	ps->b = temp;
	return (1);
}

void	pa(t_ps_struct *ps)
{
	if (push_a(ps))
		ft_printf("pa\n");
}



void	pb(t_ps_struct *ps)
{
	if (push_b(ps))
		ft_printf("pb\n");
}
