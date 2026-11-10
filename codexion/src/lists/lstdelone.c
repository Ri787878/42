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
