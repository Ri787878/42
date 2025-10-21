/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/16 10:49:48 by ridias            #+#    #+#             */
/*   Updated: 2025/09/18 14:19:17 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strcpy(char *dest, char *src)
{
	int	n;

	n = 0;
	while (src[n] != '\0')
	{
		dest[n] = src[n];
		n++;
	}
	dest[n] = '\0';
	return (dest);
}

/*
#include <stdio.h>
#include <stdlib.h>

int ft_strlen(char *str)
{
	int n;

	n = 0;
	while (str[n] != '\0')
		n++;
	return (n);
}

int main(void)
{
	char	src[] = "Maria is really nice!!";
	char	*dest;
	int	leng;

	leng = ft_strlen(src);
	dest = malloc(leng + 1);
	dest = ft_strcpy(dest, src);
	printf("The sentense ->%s<- turned to ->%s<-.", src, dest);
	return (0);
}
*/