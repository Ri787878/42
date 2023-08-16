/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/16 13:57:42 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/16 13:57:50 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
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

char	*ft_strcat(char *dest, char *src)
{
	int	i;
	int	size;
	int	size2;

	size2 = ft_strlen(src);
	size = ft_strlen(dest);
	i = 0;
	while (size + i < size + size2)
	{
		dest[size + i] = src[i];
		i++;
	}
	dest[size + i] = '\0';
	return (dest);
}

char *ft_strjoin(int size, char **strs, char *sep)
{
	int	i;
	int	maxlen;
	char	*s1;

	maxlen = 0;
	i = 0;
	if (size == 0)
		return ((char *)malloc(sizeof(char)));
	//calcular byte max de tudo
	while (i < size)
	{
		maxlen += ft_strlen(strs[i]);
		i++;
	}
	maxlen += ft_strlen(sep) * size - 1;
	//Aloca memoria
	s1 = (char *)malloc(sizeof(char) * (maxlen + 1));
	i = 0;
	while (i < size)
	{
		ft_strcat(s1, strs[i]);
		if (i < size - 1)
			ft_strcat(s1, sep);
		i++;
	}
	return (s1);
}

int	main(void)
{
	char *strings[] = {"abc", "def", "ghi"};
	char *sep = "..|..";
	int numStrings = sizeof(strings) / sizeof(strings[0]);
	char *result = ft_strjoin(numStrings, strings, sep);
	
	if (result)
	{
		printf("String concatenada: %s\n", result);
		free(result);
	}
	else
	{
		printf("Mallocfail\n");
	}
	return 0;
}