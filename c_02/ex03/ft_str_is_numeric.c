/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_numeric.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/07/31 19:22:24 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/08 21:48:57 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

#include <stdio.h>

int	ft_str_is_numeric(char *str)
{
	int	i;

	i = 0;
	if (str == NULL)
		return (1);
	while (str[i] != '\0')
	{
		if (str[i] < '0' || str[i] > '9')
			return (0);
		i++;
	}
	return (1);
}
/*
int main(void)
{
	char s1[100] = "43754765453656";

        printf("%d \n", ft_str_is_numeric(s1));
	printf("%d \n", ft_str_is_numeric("23456t45678"));
	printf("%d \n", ft_str_is_numeric(""));
}
*/
