/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_numeric.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 13:58:09 by ridias            #+#    #+#             */
/*   Updated: 2025/09/17 14:24:34 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_str_is_numeric(char *str)
{
	int	n;

	n = 0;
	if (str == NULL)
		return (1);
	while (str[n] != '\0')
	{
		if (str[n] < '0' || str[n] > '9')
			return (0);
		n++;
	}
	return (1);
}

/*
int main(void)
{
	char *str = "84616813516813218153246";
	char *str1 = "65468qawesrdtfyguhijokjgerdsrdtfyguhijokjuhygtfrd";
	char *str2 = NULL;
	printf("the string %s gives result %d\n", str, ft_str_is_numeric(str));
	printf("the string %s gives result %d\n", str1, ft_str_is_numeric(str1));
	printf("the string %s gives result %d\n", str2, ft_str_is_numeric(str2));
	return (0);
}
*/