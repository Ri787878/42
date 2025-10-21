/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcat.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/18 15:11:45 by ridias            #+#    #+#             */
/*   Updated: 2025/09/21 15:52:02 by ridias           ###   ########.fr       */
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

char	*ft_strcat(char *dest, char *src)
{
	int	i;
	int	dest_leng;
	int	src_leng;

	i = 0;
	dest_leng = ft_strlen(dest);
	src_leng = ft_strlen(src);
	while (dest_leng + i < dest_leng + src_leng)
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
	char str1[100] = "This is ", str2[] = "programiz.com";

	printf("the strig 1: %s and 2: %s\n", str1, str2);
	ft_strcat(str1, str2);
	printf("combine to be: %s\n", str1);
	return (0);
}
*/