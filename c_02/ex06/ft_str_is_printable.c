/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_printable.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/07 12:16:54 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/09 03:01:44 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <stdio.h>

int	ft_str_is_printable(char *str)
{
	int	i;

	i = 0;
	while (str[i] >= 32 && str[i] <= 127)
		i++;
	if (str[i] == '\0')
		return (1);
	else
		return (0);
}
/*
int main(void)
{
	char s1[100] = "M \nria";

        printf("%d \n", ft_str_is_printable(s1));
	printf("%d \n", ft_str_is_printable(""));
	printf("%d \n", ft_str_is_printable("r54e657fo87"));
}
*/
