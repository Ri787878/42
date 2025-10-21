/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/16 11:22:31 by ridias            #+#    #+#             */
/*   Updated: 2025/09/23 16:12:49 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strncpy(char *dest, char *src, unsigned int n)
{
	int	i;

	i = 0;
	while (src[i] != '\0' && i < (int) n)
	{
		dest[i] = src[i];
		i++;
	}
	while (i < (int)n)
	{
		dest[i] = '\0';
		i++;
	}
	return (dest);
}


#include <stdio.h>
#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
		n++;
	return (n);
}
int main(void)
{
	int	leng;
	char	src[] = "Maria is really nice!!";
	char	*dest;

	leng = ft_strlen(src);
	dest = malloc(10 + 1);
	dest = ft_strncpy(dest, src, 10);
	printf("%s", dest);
	return (0);
}
