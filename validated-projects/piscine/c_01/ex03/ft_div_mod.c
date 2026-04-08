/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_div_mod.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/14 15:18:03 by ridias            #+#    #+#             */
/*   Updated: 2025/09/16 12:23:16 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_div_mod(int a, int b, int *div, int *mod)
{
	*div = a / b;
	*mod = a % b;
}

/*
#include <stdio.h>

int main (void)
{
	int a;
	int b;

	int div0;
	int mod0;

	int *div;
	int *mod;

	a = 75;
	b = 26;
	div0 = 123;
	mod0 = 123;
	div = &div0;
	mod = &mod0;
	ft_div_mod(a, b, div, mod);
	printf("The result of the multiplication of %d by %d,", a, b);
	printf(" is %d with remainder %d.\n", *div, *mod);
	return (0);
}
*/