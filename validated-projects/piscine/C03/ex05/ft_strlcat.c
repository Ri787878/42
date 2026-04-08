/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/21 12:20:18 by ridias            #+#    #+#             */
/*   Updated: 2025/09/21 16:41:00 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_strlen(char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
		n++;
	return (n);
}

unsigned int	ft_strlcat(char *dest, char *src, unsigned int size)
{
	unsigned int	i;
	unsigned int	dest_leng;

	dest_leng = ft_strlen(dest);
	i = 0;
	while (src[i] != '\0' && i <= size)
	{
		dest[dest_leng + i] = src[i];
		i++;
	}
	dest[dest_leng + i] = '\0';
	return (dest_leng + ft_strlen(src));
}

/*
int main(void)
{
	//char str1[100] = "1337 42", str2[] = "Born to code1";
	//char str1[100] = "", str2[] = "";
	char str1[100] = "", str2[] = "hello";
	int n = 0;
	printf("the strig 1: %s and 2: %s\n", str1, str2);
	n = ft_strlcat(str1, str2, 11);
	printf("result = %d\n     combine to be:%s\n", n, str1);

	//printf("The correct result: 1337 42Born to code");
	printf("The correct result:");
	return (0);
}
*/