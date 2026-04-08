/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_lst_min.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/17 12:16:01 by ridias            #+#    #+#             */
/*   Updated: 2026/03/17 12:16:29 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

int	get_lst_min(t_list *stack)
{
	int		min;
	t_list	*temp;

	if (!stack)
		return (0);
	temp = stack;
	min = ((t_num *)temp->content)->value;
	while (temp)
	{
		if (((t_num *)temp->content)->value < min)
			min = ((t_num *)temp->content)->value;
		temp = temp->next;
	}
	return (min);
}
