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

char	*check(int size, char **strs, char *sep, char *s1)
{
	int		i;
	char	*maxlen;

	maxlen = "\0";
	i = 0;
	s1[0] = '\0';
	while (i < size)
	{
		ft_strcat(s1, strs[i]);
		if (i < size - 1)
			ft_strcat(s1, sep);
		i++;
	}
	ft_strcat(s1, maxlen);
	return (s1);
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	int		i;
	int		maxlen;
	char	*s1;

	maxlen = 0;
	i = 0;
	if (size <= 0)
	{
		s1 = (char *)malloc(sizeof(char));
		s1[0] = '\0';
		return (s1);
	}
	while (i < size)
	{
		maxlen += ft_strlen(strs[i]);
		if (i < size - 1)
			maxlen += ft_strlen(sep);
		i++;
	}
	s1 = (char *)malloc (sizeof(char) * (maxlen + 1));
	return (check(size, strs, sep, s1));
}
/*
int	main(void)
{
	char *strings[] = {"abc", "def", "123"};
	char *sep = ".";
	int numStrings = sizeof(strings) / sizeof(strings[0]);
	char *result = ft_strjoin(numStrings, strings, sep);

	printf("String concatenada: %s\n", result);
	free(result);

	return 0;
}
*/
