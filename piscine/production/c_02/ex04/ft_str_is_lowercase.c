/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_lowercase.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 14:25:09 by ridias            #+#    #+#             */
/*   Updated: 2025/09/17 14:46:51 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_str_is_lowercase(char *str)
{
	int	n;

	n = 0;
	if (str == NULL)
		return (1);
	while (str[n] != '\0')
	{
		if (str[n] < 'a' || str[n] > 'z')
			return (0);
		n++;
	}
	return (1);
}

/*
int main(void)
{
	char *str = "asfdfgE";
	char *str1 = "awesrdtfyguhijokjgerdsrdtfyguhijokjuhygtfrd";
	char *str2 = NULL;
	printf("the string %s gives result %d\n", str, ft_str_is_lowercase(str));
	printf("the string %s gives result %d\n", str1, ft_str_is_lowercase(str1));
	printf("the string %s gives result %d\n", str2, ft_str_is_lowercase(str2));
	return (0);
}
*/