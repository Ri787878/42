/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/10 21:13:01 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/10 21:13:04 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		i++;
	}
	return (i);
}

char	*ft_strdup(char *src)
{
	char	*sdup;

	sdup = malloc(sizeof(char *) * ft_strlen(src));
	sdup = src;
	return (sdup);
}
/*
int main (void)
{
	char	*w1 = "Maria";
	char	*w2;

	w2 = ft_strdup(w1);
	printf("%s \n", w2);
	return (0);
}
*/
