/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 12:40:34 by ridias            #+#    #+#             */
/*   Updated: 2025/10/29 12:54:12 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

size_t	ft_strlen(const char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
	{
		n++;
	}
	return (n);
}

char to_upper(unsigned int i, char c) {
	(void)i;  // ignore the index
	if (c >= 'a' && c <= 'z')
		return c - ('a' - 'A');
	return c;
}
char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	char	*string;
	int		t;

	t = 0;
	string = malloc(ft_strlen(s));
	while (s[t])
	{
		string[t] = f(t, s[t]);
		t++;
	}
	string[t] = '\0';
	return (string);
}

int	main(void)
{
	char	*string = "Maria is Nice!!";
	char	*result;

	result = malloc(ft_strlen(string));
	printf("The string: \"%s\", ", string);
	result = ft_strmapi(string, to_upper);
	printf("turns to become: \"%s\"\n", result);
	free(result);
	return(0);
}