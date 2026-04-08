/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/18 14:55:32 by ridias            #+#    #+#             */
/*   Updated: 2025/09/18 15:10:46 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_strncmp(char *s1, char *s2, unsigned int n)
{
	unsigned int	i;

	i = 0;
	while (i < n - 1 && (s1[i] == s2[i] && s1[i] != '\0' && s2[i] != '\0'))
		i++;
	if (n == 0)
		return (0);
	else
		return (s1[i] - s2[i]);
}

/*
int main(void)
{
	char str1[] = "Hello";
	char str2[] = "Hello";
	//char str3[] = "";
	//char str4[] = "";

	printf(" \nresult of comparison of ->%s<- and ->%s<- is %d.\n", 
	str1, str2, ft_strncmp(str1, str2, 3));
	//printf(" \nresult of comparison of ->%s<- and ->%s<- is %d.\n"
	,str2, str3, ft_strncmp(str2, str3, 3));
	//printf(" \nresult of comparison of ->%s<- and ->%s<- is %d.\n"
	,str3, str4, ft_strncmp(str3, str4, 3));
	return (0);
}
*/