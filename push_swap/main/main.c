/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/13 11:45:14 by ridias            #+#    #+#             */
/*   Updated: 2026/02/16 13:01:52 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

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
	
	
}