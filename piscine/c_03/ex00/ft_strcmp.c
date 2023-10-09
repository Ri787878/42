/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/09 00:05:55 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/12 13:50:04 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <string.h>
#include <stdio.h>

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i] != '\0' && s1[i] != '\0' && s1[i] == s2[i])
	{
		++i;
	}
	return (s1[i] - s2[i]);
}
/*
int main(void)
{
        char *s1 = "Maraia";
        char *s2 = "Maria";

        printf("%d \n", ft_strcmp(s2, s1));

	char *s3 = "Maraia";
        char *s4 = "Maria";

        printf("%d \n", strcmp(s4, s3));
}
*/
