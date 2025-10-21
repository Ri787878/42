/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/14 15:11:47 by ridias            #+#    #+#             */
/*   Updated: 2025/09/14 15:17:07 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_swap(int *a, int *b)
{
	int	temp;

	temp = *a;
	*a = *b;
	*b = temp;
}
/*
#include <stdio.h>

int main (void)
{
	int a;
	int b;
	int *a1;
	int *b1;

	a = 123;
	b = 456;
	a1 = &a;
	b1 = &b;
	printf("The old order is a: %d and b is: %d\n", *a1, *b1);
	ft_swap(a1, b1);
	printf("The new order is a: %d and b is: %d", *a1, *b1);
}
*/