/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 15:58:29 by ridias            #+#    #+#             */
/*   Updated: 2025/09/23 12:06:12 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>

unsigned int	ft_strlcpy(char *dest, char *src, unsigned int size)
{
	int	n;

	n = 0;
	if (dest == NULL || src == NULL)
		return (size);
	if (size <= 0)
		return (size);
	while (n < (int)size - 1)
	{
		dest[n] = src[n];
		n++;
	}
	dest[n] = '\0';
	return (n);
}
/*
int main(void)
{
	//printf("src[%d] = %c && dest[%d] = %c", n, src[n], n, src[n]);
	
	char str1[15];
	char *str2 = "0987654321";
	//char *str2 = NULL;
	
	// ft_strlcpy(str2, str1, ft_strlen(str2) + ft_strlen(str1));
	printf("the result %d\n", ft_strlcpy(str2, str1, 10));
	// printf("the string %s gives result %d\n", str, ft_str_is_lowercase(str));
	// printf("the string %s gives result %d\n", str1, 
	ft_str_is_lowercase(str1));
	printf("the string %s \n", str2);
	return (0);
}
*/