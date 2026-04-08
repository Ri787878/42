/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 12:44:51 by ridias            #+#    #+#             */
/*   Updated: 2025/10/16 12:46:04 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
	{
		n++;
	}
	return (n);
}

char	*ft_strdup(char *src)
{
	int		n;
	char	*str;

	n = 0;
	str = malloc(ft_strlen(src));
	while (src[n])
	{
		str[n] = src[n];
		n++;
	}
	str[n] = '\0';
	return (str);
}
