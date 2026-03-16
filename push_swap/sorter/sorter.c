/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sorter.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/14 19:15:58 by ridias            #+#    #+#             */
/*   Updated: 2026/03/16 14:47:28 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

static int	get_max_bits(int max_value)
{
	int	bits;

	bits = 0;
	while ((max_value >> bits) != 0)
		bits++;
	return (bits);
}

static void	get_index(t_list *stack, int *arr, int size)
{
	t_list	*ptr;
	int		i;

	ptr = stack;
	while (ptr)
	{
		i = 0;
		while (i < size)
		{
			if (((t_num *)ptr->content)->value == arr[i])
			{
				((t_num *)ptr->content)->index = i;
				break ;
			}
			i++;
		}
		ptr = ptr->next;
	}
}

static void	sort_int_array(int *arr, int size)
{
	int	i;
	int	j;
	int	temp;

	i = 0;
	while (i < size)
	{
		j = i + 1;
		while (j < size)
		{
			if (arr[i] > arr[j])
			{
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
			j++;
		}
		i++;
	}
}

void	normalize_stack(t_list *stack)
{
	int		*arr;
	int		size;
	int		i;
	t_list	*ptr;

	size = ft_lstsize(stack);
	arr = malloc(sizeof(int) * size);
	if (!arr)
		return ;
	ptr = stack;
	i = 0;
	while (i < size)
	{
		arr[i] = ((t_num *)ptr->content)->value;
		ptr = ptr->next;
		i++;
	}
	sort_int_array(arr, size);
	get_index(stack, arr, size);
	free(arr);
}

void	radixsort(t_ps_struct *ps)
{
	int	size;
	int	max_bits;
	int	bit;
	int	i;
	t_num	*node;

	if (!ps || !ps->a || !ps->a->next)
		return ;
	size = ft_lstsize(ps->a);
	max_bits = get_max_bits(size - 1);
	bit = 0;
	while (bit < max_bits)
	{
		i = 0;
		while (i < size)
		{
			node = (t_num *)ps->a->content;
			if (((node->index >> bit) & 1) == 1)
				ra(ps);
			else
				pb(ps);
			i++;
		}
		while (ps->b)
			pa(ps);
		bit++;
	}
}

