#include "../codexion.h"


void	lstadd_back(t_list **lst, t_list *new)
{
	t_list	*position;

	if (!lst || !new)
		return ;
	if (!*lst){
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
