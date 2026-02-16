/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/26 16:31:13 by andqueir          #+#    #+#             */
/*   Updated: 2026/02/16 12:48:05 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

t_list	*ft_lstlast(t_list *lst)
{
	if (!lst)
		return (NULL);
	if (!lst->next)
		return (lst);
	return (ft_lstlast(lst->next));
}

/* t_list *create_node(char *content)
{
	t_list *node = malloc(sizeof(t_list));
	if (!node)
		return (NULL);
	node->content = content;
	node->next = NULL;
	return node;
}

int	main()
{
	t_list *last;

	last = ft_lstlast(NULL);
	printf("Test 1 (Empty list): %s\n", last ? "Failed" : "Passed");

	t_list *single = create_node("only");
	last = ft_lstlast(single);
	if (last == single)
		printf("Test 2 (Single node): Passed, content = %s\n",
		(char *)last->content);
	else
		printf("Test 2 (Single node): Failed\n");
	free(single);

	t_list *node1 = create_node("first");
	t_list *node2 = create_node("second");
	t_list *node3 = create_node("third");

	node1->next = node2;
	node2->next = node3;
	node3->next = NULL;

	last = ft_lstlast(node1);
	if (last == node3)
		printf("Test 3 (Multi-node): Passed, content = %s\n",
		(char *)last->content);
	else
		printf("Test 3 (Multi-node): Failed\n");

	free(node1);
	free(node2);
	free(node3);

	return (0);
} */
