/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simple_sorter.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/17 12:14:39 by ridias            #+#    #+#             */
/*   Updated: 2026/03/17 13:06:28 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

void	organized_sort(t_ps_struct *ps)
{
	if (ps->stack_size == 2)
	{
		if (!is_sorted(ps->a))
			sa(ps);
	}
	else if (ps->stack_size == 3)
	{
		if (!is_sorted(ps->a))
			sort_3(ps);
	}
	else if (ps->stack_size == 4)
	{
		if (!is_sorted(ps->a))
			sort_4(ps);
	}
	else if (ps->stack_size == 5)
	{
		if (!is_sorted(ps->a))
			sort_5(ps);
	}
}

int	get_node_index(t_list *stack, int target_value)
{
	int		index;
	t_list	*temp;

	index = 0;
	temp = stack;
	while (temp)
	{
		if (((t_num *)temp->content)->value == target_value)
			return (index);
		index++;
		temp = temp->next;
	}
	return (-1);
}

void	sort_3(t_ps_struct *ps)
{
	int		lst_max;
	t_list	*first;
	t_list	*second;

	if (!ps || !ps->a)
		return ;
	lst_max = get_lst_max(ps->a);
	first = ps->a;
	second = first->next;
	if (((t_num *)first->content)->value == lst_max)
		ra(ps);
	else if (((t_num *)second->content)->value == lst_max)
		rra(ps);
	first = ps->a;
	second = first->next;
	if (((t_num *)first->content)->value > ((t_num *)second->content)->value)
		sa(ps);
}

void	sort_4(t_ps_struct *ps)
{
	int	min;
	int	index;

	if (!ps || !ps->a)
		return ;
	min = get_lst_min(ps->a);
	index = get_node_index(ps->a, min);
	if (index == 1)
		ra(ps);
	else if (index == 2)
	{
		ra(ps);
		ra(ps);
	}
	else if (index == 3)
		rra(ps);
	pb(ps);
	sort_3(ps);
	pa(ps);
}

void	sort_5(t_ps_struct *ps)
{
	int	min;
	int	index;

	if (!ps || !ps->a)
		return ;
	min = get_lst_min(ps->a);
	index = get_node_index(ps->a, min);
	if (index <= 2)
	{
		while (((t_num *)ps->a->content)->value != min)
			ra(ps);
	}
	else
	{
		while (((t_num *)ps->a->content)->value != min)
			rra(ps);
	}
	pb(ps);
	sort_4(ps);
	pa(ps);
}
