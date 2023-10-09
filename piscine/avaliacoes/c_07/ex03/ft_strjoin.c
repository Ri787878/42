/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ljorge-r <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/15 08:39:13 by ljorge-r          #+#    #+#             */
/*   Updated: 2023/08/16 10:24:37 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

int	ft_str_length(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

char	*ft_strcpy(char *dest, char *src)
{
	int	i;

	i = 0;
	while (src[i] != '\0')
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = '\0';
	return (dest);
}

int	ft_total_length(char **strings, int size, char *sep)
{
	int	total_length;
	int	sep_length;
	int	i;

	sep_length = ft_str_length(sep);
	total_length = 0;
	i = 0;
	while (i < size)
	{
		total_length += ft_str_length(strings[i]);
		i++;
	}
	total_length += sep_length * (size - 1);
	return (total_length);
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	int		total_length;
	int		index;
	char	*final;

	if (size == 0)
		return ((char *)malloc(sizeof(char)));
	total_length = ft_total_length(strs, size, sep);
	final = (char *)malloc((total_length + 1) * sizeof(char));
	if (final == NULL)
		return (NULL);
	index = 0;
	while (index < size)
	{
		ft_strcpy(final, strs[index]);
		final += ft_str_length(strs[index]);
		if (index < size - 1)
		{
			ft_strcpy(final, sep);
			final += ft_str_length(sep);
		}
		index++;
	}
	return (final - total_length);
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
