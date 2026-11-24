#include "../codexion.h"


int	lstiter(t_list *lst, int (*f)(void *))
{
	if (lst && f)
	{
		while (lst)
		{
			if (f(lst->content) <= 0)
				return (-1);
			lst = lst->next;
		}
	}
	return (1);
}
