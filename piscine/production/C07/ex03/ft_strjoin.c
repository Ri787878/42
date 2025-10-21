/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/26 10:57:59 by ridias            #+#    #+#             */
/*   Updated: 2025/09/29 10:46:43 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
	{
		n++;
	}
	return (n);
}

char	*sum_strings(int size, char **strs, char *sep)
{
	int		n;
	int		i;
	int		counter;
	char	*result;

	n = 0;
	i = 0;
	counter = 0;
	if (size <= 0)
		counter = 1;
	else
	{
		while (n < size)
		{
			counter += ft_strlen(strs[n]);
			n++;
		}
		counter += ft_strlen(sep) * (size - 1);
	}
	result = (char *) malloc(counter * sizeof(char));
	if (result == NULL)
		return (0);
	return (result);
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	int		n;
	int		i;
	int		c;
	char	*result;

	result = sum_strings(size, strs, sep);
	n = 0;
	i = 0;
	c = 0;
	while (n < size)
	{
		i = 0;
		while (strs[n][i])
			result[c++] = strs[n][i++];
		i = 0;
		while (sep[i] && n != size - 1)
			result[c++] = sep[i++];
		n++;
	}
	result[c] = '\0';
	return (result);
}

/* int main(void)
{
	char *strs[] = {"Hello", "world", "this", "is", "a", "test"};
	int size = 6;
	char *sep = "||";
	char *all_together = ft_strjoin(size, strs, sep);

	printf("New string: %s\n", all_together);
	free(all_together);
} */