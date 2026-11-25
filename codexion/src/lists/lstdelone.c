/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   lstdelone.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/11/25 09:58:18 by ridias            #+#    #+#             */
/*   Updated: 2026/11/25 10:02:04 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../codexion.h"

void	lstdelone(t_list **lst, t_list *node, void (*del)(void *))
{
	if (!lst || !*lst || !node || !del)
		return ;
	if (node->previous)
		node->previous->next = node->next;
	else
		*lst = node->next;
	if (node->next)
		node->next->previous = node->previous;
	node->next = NULL;
	node->previous = NULL;
	del(node->content);
	free(node);
}
