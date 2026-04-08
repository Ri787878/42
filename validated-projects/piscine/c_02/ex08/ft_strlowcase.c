/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlowcase.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 15:24:13 by ridias            #+#    #+#             */
/*   Updated: 2025/09/17 15:58:07 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

char	*ft_strlowcase(char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
	{
		if ('A' <= str[n] && str[n] <= 'Z')
			str[n] = str[n] + 32;
		n++;
	}
	return (str);
}

/*
int main(void)
{
	char	str[] = "Maria is REALLY nice!!";

	printf("The sentense ->%s<-", str);
	printf(" \nturns to ->%s<-.", ft_strlowcase(str));
	return (0);
}
*/