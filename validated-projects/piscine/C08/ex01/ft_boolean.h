/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_boolean.h                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/28 17:38:32 by ridias            #+#    #+#             */
/*   Updated: 2025/09/29 12:14:39 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <unistd.h>
#define FT_BOOLEAN_H

#ifdef FT_BOOLEAN_H

typedef int	t_bool;
# define TRUE 1
# define FALSE 0

# define EVEN(nbr) !((nbr) % 2 == 0)
# define SUCCESS 0
# define ODD_MSG "I have an odd number of arguments.\n"
# define EVEN_MSG "I have an even number of arguments."

void	ft_putstr(char *c);
t_bool	ft_is_even(int nbr);

#endif