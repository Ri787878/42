/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/18 16:57:15 by ridias            #+#    #+#             */
/*   Updated: 2025/09/21 12:12:54 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int	sub_string_check(char *str, char *to_find)
{
	while (*str == *to_find)
	{
		if (*to_find == '\0')
			return (1);
		if (*str == '\0')
			return (-1);
		str++;
		to_find++;
	}
	if (*to_find == '\0')
		return (1);
	else
		return (-1);
}

char	*ft_strstr(char *str, char *to_find)
{
	char	*dest;

	dest = str;
	while (*dest)
	{
		if (sub_string_check(dest, to_find) == 1)
			return (dest);
		dest++;
	}
	return (NULL);
}

/*
int main(void)
{
	char str1[] = "ola eu estou na 42 e quero desistir.", str2[] = "";
	char *res;
	printf("origem: %s \nencontra: %s\n \n", str1, str2);
	res = ft_strstr(str1, str2);
	printf("Resultado: %s\n", res);
	return (0);
}
*/