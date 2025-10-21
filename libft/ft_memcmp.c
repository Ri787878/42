/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 16:40:06 by ridias            #+#    #+#             */
/*   Updated: 2025/10/21 16:55:57 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>
#include <stdio.h>

int ft_memcmp(const void *s1, const void *s2, size_t n)
{
	const unsigned char	*p_s1;
	const unsigned char	*p_s2;
	int					i;

	p_s1 = (const unsigned char *)s1;
	p_s2 = (const unsigned char *)s2;
	i = 0;
	if ((int)n == 0)
		return (0);
	while (i < (int)n && p_s1[i] == p_s2[i] && p_s1[i] != '\0' && p_s2[i] != '\0')
		i++;
	if (p_s1[i] == '\0' && p_s2[i] != '\0')
		return (-p_s2[i]);
	if (p_s1[i] != '\0' && p_s2[i] == '\0')
		return (p_s1[i]);
	return (0);
}

int main (void)
{
	char	tests[4][27] = {"abcdefghijklmnopqrstuvwxyz", "Maria is nice!!", "0123456789", "the \t tab is tabb\ting"};
	int	result_true;
	int	result;
	int		n = 0;
	int		size = 4;

	while (n < size)
	{
		result = ft_memcmp(tests[n], tests[0], 5);
		result_true = memcmp(tests[n], tests[0], 5);
		printf("\nThe frase \"%s\" && comparing \"%s\"\n", tests[n], tests[0]);
		printf("MINE result is \t\"%d\"\n", result);
		printf("THEI result is \t\"%d\"\n", result_true);
		n++; 
	}
	return (0);
}