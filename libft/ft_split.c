/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 13:56:02 by ridias            #+#    #+#             */
/*   Updated: 2025/10/29 11:19:35 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	word_counter(char *s, char c)
{
	int	word_counter;
	int	index;

	index = 0;
	word_counter = 0;
	while (s[index] != '\0')
	{
		if (s[index] != c && (index == 0 || s[index - 1] == c))
			word_counter++;
		index++;
	}
	return (word_counter);
}

char	*ft_strncpy(char *dest, char *src, unsigned int n)
{
	int	i;

	i = 0;
	while (src[i] != '\0' && i < (int)n)
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

char	**create_array(char **array, char *s, char c, int index)
{
	int	n;
	int	word_start;

	n = 0;
	while (s[index])
	{
		if (s[index] != c && (index == 0 || s[index - 1] == c))
		{
			word_start = index;
			while (s[index] && s[index] != c)
				index++;
			array[n] = malloc(index - word_start + 1);
			if (!array[n])
				return (NULL);
			ft_strncpy(array[n], s + word_start, index - word_start);
			array[n++][index - word_start] = '\0';
		}
		else
			index++;
	}
	array[n] = NULL;
	return (array);
}

char	**ft_split(char const *s, char c)
{
	char	**array;
	int		index;

	index = 0;
	if (!s)
		return (NULL);
	array = malloc((word_counter((char *)s, c) + 1) * sizeof(char *));
	if (!array)
		return (NULL);
	return (create_array(array, (char *)s, c, index));
}
