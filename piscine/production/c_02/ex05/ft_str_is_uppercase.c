/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_uppercase.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 14:33:20 by ridias            #+#    #+#             */
/*   Updated: 2025/09/17 14:47:09 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_str_is_uppercase(char *str)
{
	int	n;

	n = 0;
	if (str == NULL)
		return (1);
	while (str[n] != '\0')
	{
		if (str[n] < 'A' || str[n] > 'Z')
			return (0);
		n++;
	}
	return (1);
}

/*
int main(void)
{
	char *str = "SDFGHFDS";
	char *str1 = "SADFGDAFs";
	char *str2 = NULL;
	printf("the string %s gives result %d\n", str, ft_str_is_uppercase(str));
	printf("the string %s gives result %d\n", str1, ft_str_is_uppercase(str1));
	printf("the string %s gives result %d\n", str2, ft_str_is_uppercase(str2));
	return (0);
}
*/