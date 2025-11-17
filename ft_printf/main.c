/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 16:21:01 by ridias            #+#    #+#             */
/*   Updated: 2025/11/17 12:17:09 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <stdio.h>

int	main(void)
{
	char			*str;
	unsigned int	u_int_v;

	u_int_v = 4294967295;
	str = "MARIA IS THE bEST";
	/* ft_printf("The function woks no variables.\n");
	ft_printf("The function woks no variables = \"%\".\n");
	ft_printf("The function woks no variables = \"%%\".\n");
	ft_printf("The function woks no variables = \"%%%\".\n");
	ft_printf("The function woks variable = \"%c\".\n", 'P');
	ft_printf("The function woks string = \"%s\".\n", str);
	ft_printf("The function woks int = \"%d\".\n", -12345678);
	ft_printf("The function woks dud ptr = \"%p\".\n", NULL);
	ft_printf("The function woks dud ptr = \"%p\".\n", &str);
	ft_printf("The function woks uint = \"%u\".\n", u_int_v);
	ft_printf("The function woks hexa x = \"%x\".\n", 0);
	ft_printf("The function woks hexa X = \"%X\".\n", 0);
	ft_printf("The function woks hexa x = \"%x\".\n", u_int_v);
	ft_printf("The function woks hexa X = \"%X\".\n", u_int_v);
	ft_printf("The function woks hexa x = \"%x\".\n", 1234567890);
	ft_printf("The function woks hexa X = \"%X\".\n", 1234567890); */
	
	ft_printf("The function woks hexa X = \"%y\".\n", 1234567890);
	printf("The function woks hexa X = \"%y\".\n", 1234567890);
	ft_printf("The function woks hexa X = \"%c\".\n", 1);
	printf("The function woks hexa X = \"%c\".\n", 1);

	return (0);
}
