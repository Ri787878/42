/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcapitalize.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/07 12:19:39 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/08 22:31:39 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <stdio.h>

char	*ft_strlowcase(char	*str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] >= 'A' && str[i] <= 'Z')
			str[i] = str[i] + 32;
		i++;
	}
	return (str);
}

char	*ft_strcapitalize(char	*str)
{
	int	i;
	int	j;

	j = 1;
	i = 0;
	ft_strlowcase(str);
	while (str[i] != '\0')
	{
		if (str[i] >= 'a' && str[i] <= 'z')
		{
			if (j == 1)
				str[i] = str[i] - 32;
			j = 0;
		}
		else if (str[i] >= '0' && str[i] <= '9')
		{
			j = 0;
		}
		else
			j = 1;
		i++;
	}
	return (str);
}
/*
int main(void)
{
	char s1[100] = "ola, tudo bem? 42palavras quarenta-e-duas; cinquenta+e+um";
	char *s2 = ft_strcapitalize(s1);
        printf("%s \n", s2);
	printf("Ola, Tudo Bem? 42palavras Quarenta-E-Duas; Cinquenta+E+Um\n");
}
*/
