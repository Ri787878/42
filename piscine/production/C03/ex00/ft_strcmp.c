/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 17:11:57 by ridias            #+#    #+#             */
/*   Updated: 2025/09/18 15:11:05 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i] == s2[i] && s1[i] != '\0' && s2[i] != '\0')
		i++;
	return (s1[i] - s2[i]);
}

/*
int main(void)
{
	char str1[] = "Hello";
	char str2[] = "Hello";
	char str3[] = "";
	char str4[] = "";

	printf(" \nresult of comparison of ->%s<- and ->%s<- is %d.\n", 
	str1, str2, ft_strcmp(str1, str2));
	printf(" \nresult of comparison of ->%s<- and ->%s<- is %d.\n", 
	str2, str3, ft_strcmp(str2, str3));
	printf(" \nresult of comparison of ->%s<- and ->%s<- is %d.\n", 
	str3, str4, ft_strcmp(str3, str4));
	return (0);
}
*/