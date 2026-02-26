/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/23 15:14:02 by ridias            #+#    #+#             */
/*   Updated: 2026/02/26 12:11:25 by ridias           ###   ########.fr       */
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

static void	clrs(char **parts)
{
	int	k;

	if (!parts)
		return ;
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
			if (!dup)
				return (clrs(parts), ft_lstclear(&ps->a, free), -1);
			ps->temp_node = ft_lstnew(dup);
			if (!ps->temp_node)
				return (free(dup), clrs(parts), ft_lstclear(&ps->a, free), -1);
			ft_lstadd_back(&ps->a, ps->temp_node);
			j++;
		}
		clrs(parts);
		i++;
	}
	return (0);
}

/*
int main(void)
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
}*/
