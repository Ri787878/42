/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_printable.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 14:36:04 by ridias            #+#    #+#             */
/*   Updated: 2025/09/18 14:24:17 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_str_is_printable(char *str)
{
	int	i;

	i = 0;
	while (str[i] >= 32 && str[i] <= 127)
		i++;
	if (str[i] == '\0')
		return (1);
	else
		return (0);
}

/*
int main(void)
{
	char *str = "SDFGHFDS";
	char *str1 = "SADFGDAF\ts";
	char *str2 = NULL;
	printf("the string %s gives result %d\n", str, ft_str_is_printable(str));
	printf("the string %s gives result %d\n", str1, ft_str_is_printable(str1));
	printf("the string %s gives result %d\n", str2, ft_str_is_printable(str2));
	return (0);
}
*/