/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_int_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/14 16:54:28 by ridias            #+#    #+#             */
/*   Updated: 2025/09/16 12:16:43 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>

void	ft_rev_int_tab(int *tab, int size)
{
	int	n;
	int	end;
	int	caar;

	n = 0;
	end = size;
	while (n < end)
	{
		caar = tab[n];
		tab[n] = tab[end - 1];
		tab[end - 1] = caar;
		end--;
		n++;
	}
}

/*
int main(void)
{
	int str[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	int n = 0;
	// int *str1 = &str;

	printf("The order is -> ");
	while (n < 10)
	{
		printf("%d ", str[n]);
		n++;
	}
	printf("<-.\n");
	n = 0;
	ft_rev_int_tab(str, 10);
	printf("turns to  -> ");
	while (n < 10)
	{
		printf("%d ", str[n]);
		n++;
	}
	printf("<-.");

	return (0);
}
*/