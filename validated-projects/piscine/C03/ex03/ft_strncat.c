/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/18 16:20:57 by ridias            #+#    #+#             */
/*   Updated: 2025/09/21 16:16:40 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		i++;
	}
	return (i);
}

char	*ft_strncat(char *dest, char *src, unsigned int nb)
{
	unsigned int	i;
	unsigned int	dest_leng;

	dest_leng = ft_strlen(dest);
	i = 0;
	while (src[i] != '\0' && i < nb)
	{
		dest[dest_leng + i] = src[i];
		i++;
	}
	dest[dest_leng + i] = '\0';
	return (dest);
}

/*
int main(void)
{
	char str1[100] = "Hello", str2[] = "World";

	printf("the strig 1: %s and 2: %s\n", str1, str2);
	ft_strncat(str1, str2, 5);
	printf("combine to be: %s\n", str1);
	printf("suppose to be: HelloWo\n");
	return (0);
}
*/