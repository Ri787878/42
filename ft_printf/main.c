/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 16:21:01 by ridias            #+#    #+#             */
/*   Updated: 2025/11/13 16:39:57 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	main(void)
{
	ft_printf("The function woks when given no variables.\n");

	ft_printf("The function woks when given one variable = \"%c\".\n", 'P');

	ft_printf("The function woks when given one string = \"%s\".\n", "Vanessa");

	ft_printf("The function woks when given one int = \"%d\".\n", 195);


	return (0);
}
