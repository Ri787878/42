/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   lstadd_back.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/11/25 09:58:07 by ridias            #+#    #+#             */
/*   Updated: 2026/11/25 10:02:19 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../codexion.h"

void	lstadd_back(t_list **lst, t_list *new)
{
	t_list	*position;

	if (!lst || !new)
		return ;
	if (!*lst)
	{
		new->previous = NULL;
		new->next = NULL;
		*lst = new;
	}
	else
	{
		position = lstlast(*lst);
		position->next = new;
		new->previous = position;
		new->next = NULL;
	}
}
