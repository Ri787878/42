#include "../codexion.h"


t_list	*lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*new_list;
	t_list	*new_node;
	void	*content;

	if (!lst || !f)
		return (NULL);
	new_list = NULL;
	new_node = NULL;
	while (lst)
	{
		content = f(lst->content);
		new_node = lstnew(content);
		if (!new_node)
		{
			del(content);
			lstclear(&new_list, del);
			return (NULL);
		}
		lstadd_back(&new_list, new_node);
		lst = lst->next;
	}
	return (new_list);
}
