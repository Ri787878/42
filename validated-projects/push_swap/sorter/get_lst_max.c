/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_lst_max.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/17 12:15:24 by ridias            #+#    #+#             */
/*   Updated: 2026/03/17 18:24:39 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

int	get_lst_max(t_list *stack)
{
	int		max;
	t_list	*temp;

	if (!stack)
		return (0);
	temp = stack;
	max = ((t_num *)temp->content)->value;
	while (temp != NULL)
	{
		if (((t_num *)temp->content)->value > max)
			max = ((t_num *)temp->content)->value;
		temp = temp->next;
	}
	return (max);
}
