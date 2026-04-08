/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_div_mod.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/14 16:11:49 by ridias            #+#    #+#             */
/*   Updated: 2025/09/14 16:23:09 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_ultimate_div_mod(int *a, int *b)
{
	int	temp;

	temp = *a;
	*a = *a / *b;
	*b = temp % *b;
}

/*
#include <stdio.h>

int main (void)
{
	int a;
	int b;
	int *a1;
	int *b1;

	a = 75;
	b = 26;
	a1 = &a;
	b1 = &b;
	printf("The result of the multiplication of %d by %d,", *a1, *b1);
	ft_ultimate_div_mod(a1, b1);
	printf(" is %d with remainder %d.\n", *a1, *b1);
	return (0);
}
*/