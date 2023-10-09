/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcat.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/09 04:33:53 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/09 04:33:59 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <stdio.h>
#include <string.h>

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

char	*ft_strcat(char *dest, char *src)
{
	int	i;
	int	size;
	int	size2;

	size2 = ft_strlen(src);
	size = ft_strlen(dest);
	i = 0;
	while (size + i < size + size2)
	{
		dest[size + i] = src[i];
		i++;
	}
	dest[size + i] = '\0';
	return (dest);
}
/*
int main(void)
{
	char s1[12] = "MAria";
	char s2[10] = "123";

	printf("%s \n", ft_strcat(s2, s1));

	char s3[12] = "MAria";
	char s4[10] = "123";

	printf("%s \n", strcat(s4, s3));
}
*/
