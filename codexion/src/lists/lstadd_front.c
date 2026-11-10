#include "../codexion.h"

void	lstadd_front(t_list **lst, t_list *new)
{
	if (lst != NULL && new != NULL)
	{
		new->previous = NULL;
		new->next = *lst;
		if (*lst)
			(*lst)->previous = new;
		*lst = new;
	}
}
