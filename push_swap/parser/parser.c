/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/23 15:14:02 by ridias            #+#    #+#             */
/*   Updated: 2026/02/25 17:25:03 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"
/*
char	*parser(char *args)
{
	int	nums[];

	while (args[i] != '\0')
	{

		i++;
	}
}
*/

void	ps_init(t_ps_struct *ps)
{
	ps->cmds = NULL;
	ps->cmd_count = 0;
	ps->head = NULL;
	ps->temp_node = NULL;
}

void	print_content(void *content)
{
	ft_printf("%s\n", (char *)content);
}

int	main(int argc, char **argv)
{
	t_ps_struct	ps;
	int			i;

	ps_init(&ps);
	if (argc < 2)
		return (0);
	else if (collect_tokens(argc, argv, &ps) != 0)
	{
		ft_printf("Error\n");
		return (1);
	}
	ft_lstclear(&ps.head, free);
}

static void	free_split(char **parts)
{
	int	k;

	if (!parts)
		return;
	k = 0;
	while (parts[k])
		free(parts[k++]);
	free(parts);
}

int	collect_tokens(int argc, char **argv, t_ps_struct *ps)
{
	char	**parts;
	int		i;
	int		j;
	char	*dup;

	i = 1;
	while (i < argc)
	{
		parts = ft_split(argv[i], ' ');
		if (!parts)
			return (ft_lstclear(&ps->head, free), -1);
		j = 0;
		while (parts[j])
		{
			dup = ft_strdup(parts[j]);
			if(!dup)
				return (free_split(parts), ft_lstclear(&ps->head, free), -1);
			ps->temp_node = ft_lstnew(dup);
			if (!ps->temp_node)
				return (free(dup), free_split(parts), ft_lstclear(&ps->head, free), -1);
			ft_lstadd_back(&ps->head, ps->temp_node);
			j++;
		}
		free_split(parts);
		i++;
	}
	return (0);
}


/*int main(void)
{
	size_t i = 0;
	char **strf = ft_split(NULL, 'c');
	if (strf == NULL)
	{
		printf("ft_split returned NULL (as expected)\n");
		return (0);
	}
	while(strf[i])
	{
		printf("%s\n", strf[i]);
		i++;
	}
	free (strf);
	return (0);
}


	t_list	*head = ft_lstnew("Hello");
	t_list	*n1 = ft_lstnew("world");
	t_list **lst = &head;
	ft_lstadd_back(NULL, n1);
	t_list	*tmp = *lst;
	while (tmp != NULL)
	{
		printf("%s\n", (char *)tmp->content);
		tmp = tmp->next;
	}
*/
