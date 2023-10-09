/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_alpha.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/07/31 18:52:49 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/08 21:42:33 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <stdio.h>

int	ft_str_is_alpha(char *str)
{
	int	i;

	i = 0;
	if (str == NULL)
		return (1);
	while (str[i] != '\0' )
	{
		if ((str[i] < 'a' || str[i] > 'z') && (str[i] < 'A' || str[i] > 'Z'))
			return (0);
		i++;
	}
	return (1);
}
/*
int main(void)
{
	char s1[100] = "M1ria";

        ft_str_is_alpha(s1);
        printf("%d \n", ft_str_is_alpha(s1));
	printf("%d \n", ft_str_is_alpha("qwertyu"));
	printf("%d \n", ft_str_is_alpha(""));
}
*/
