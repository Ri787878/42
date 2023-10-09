/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_uppercase.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/07 12:15:12 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/08 22:01:14 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <stdio.h>

int	ft_str_is_uppercase(char *str)
{
	int	i;

	i = 0;
	if (str == NULL)
		return (1);
	while (str[i] != '\0' )
	{
		if (str[i] < 'A' || str[i] > 'Z')
			return (0);
		i++;
	}
	return (1);
}
/*
int main(void)
{
	char s1[100] = "M'ria";

        printf("%d \n", ft_str_is_uppercase(s1));
	printf("%d \n", ft_str_is_uppercase(""));
	printf("%d \n", ft_str_is_uppercase("QWERTYU"));
}
*/
