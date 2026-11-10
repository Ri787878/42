#include "../codexion.h"


void	lstclear(t_list **lst, void (*del)(void*))
{
	t_list	*next;
	t_list	*current;

	if (lst && del)
	{
		current = *lst;
		while (current)
		{
			next = current->next;
			current->previous = NULL;
			current->next = NULL;
			del(current->content);
			free(current);
			current = next;
		}
		*lst = NULL;
	}
}
