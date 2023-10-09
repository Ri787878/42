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
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

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
	int		b;
	char	*sdup;

	b = 0;
	sdup = (char *)malloc (ft_strlen(src));
	while (src[b] != '\0')
	{
		sdup[b] = src[b];
		b++;
	}
	sdup[b] = '\0';
	return (sdup);
}
/*
int	main(void)
{
	int		i;
	char	*w1= "Maria";
	char	*w2;

	i = 0;
	w2 = ft_strdup(w1);
	printf("%s \n", w2);
	return (0);
}
*/
