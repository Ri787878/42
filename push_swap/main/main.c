/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/13 11:45:14 by ridias            #+#    #+#             */
/*   Updated: 2026/02/26 12:02:22 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

/*
void	push_swap(char	*arg_list)
{
	t_list	*lst;
	char	*lst_cmds;

	//Check parameters of function
	//If there are no parameters return an empty prompt
	if (is_empty(arg_list))
		return ;
	//Separate the arguments into the list of ints
	//NEED to change split to create args inside of a linked list
	//List order is FIFO
	//In case of error display "Error\n"
	//Error examples:
	//		some arguments not being ints
	//		some arguments exceedeing int limits
	//		and / or presene of duplicates
	if (!split(arg_list, lst))
		{
			//NOT SURE if i need to free here or not
			ft_printf("Error\n");
			return(0);
		}
	lst_cmds = ft_sort(lst);
	//Print used cmds list by order seperated by '\n' char
	ft_printf("%s", lst_cmds);


}*/

static	void	ps_init(t_ps_struct *ps)
{
	ps->cmds = NULL;
	ps->cmd_count = 0;
	ps->head = NULL;
	ps->temp_node = NULL;
}

int	main(int argc, char **argv)
{
	t_ps_struct	ps;

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
