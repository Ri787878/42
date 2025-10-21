/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_alpha.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 12:16:26 by ridias            #+#    #+#             */
/*   Updated: 2025/09/17 14:29:59 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_str_is_alpha(char *str)
{
	int	n;

	n = 0;
	if (str == NULL)
		return (1);
	while (str[n] != '\0')
	{
		if ((str[n] < 'a' || str[n] > 'z') && (str[n] < 'A' || str[n] > 'Z'))
			return (0);
		n++;
	}
	return (1);
}

/*
int main(void)
{
	char *str = "qawesrdtfyguhijokjgerdsrdtfyguhijokjuhygtfrd1";
	char *str1 = "qawesrdtfyguhijokjgerdsrdtfyguhijokjuhygtfrd";
	char *str2 = "qawesrdtfyguhijokjgerdsrdtfyguhijokjuhygtfrd\n";
	printf("the string %s gives result %d\n", str, ft_str_is_alpha(str));
	printf("the string %s gives result %d\n", str1, ft_str_is_alpha(str1));
	printf("the string %s gives result %d\n", str2, ft_str_is_alpha(str2));
	return (0);
}
*/