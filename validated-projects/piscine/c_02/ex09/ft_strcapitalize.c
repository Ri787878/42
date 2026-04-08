/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcapitalize.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 15:26:21 by ridias            #+#    #+#             */
/*   Updated: 2025/09/17 15:57:21 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

char	*ft_strcapitalize(char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
	{
		if (n == 0 && 'a' <= str[n] && str[n] <= 'z')
			str[n] = str[n] - 32;
		if ('a' <= str[n] && str[n] <= 'z')
		{
			if (str[n - 1] == '-')
				str[n] = str[n] - 32;
			if (str[n - 1] == ' ')
				str[n] = str[n] - 32;
			if (str[n - 1] == '+')
				str[n] = str[n] - 32;
		}
		n++;
	}
	return (str);
}

/*
int main(void)
{
	char str[] = "hi, how are you? 42words forty-two; fifty+and+one";

	printf(" \nturns to ->%s<-.\n", ft_strcapitalize(str));
	printf("Result   ->Hi, How Are You? 42words 
	Forty-Two; Fifty+And+One\n"); return (0);
}
*/