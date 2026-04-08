/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strupcase.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 14:48:08 by ridias            #+#    #+#             */
/*   Updated: 2025/09/17 15:23:46 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

char	*ft_strupcase(char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
	{
		if ('a' <= str[n] && str[n] <= 'z')
			str[n] = str[n] - 32;
		n++;
	}
	return (str);
}

/*
int main(void)
{
	char	str[] = "Maria is really nice!!";

	printf("The sentense ->%s<-", str);
	printf(" \nturns to ->%s<-.", ft_strupcase(str));
	return (0);
}
*/