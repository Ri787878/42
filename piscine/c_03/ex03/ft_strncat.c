/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/09 04:34:18 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/09 04:34:26 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <string.h>
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

char	*ft_strncat(char *dest, char *src, unsigned int nb)
{
	unsigned int	i;
	unsigned int	size;
	unsigned int	size2;

	size2 = ft_strlen(src);
	size = ft_strlen(dest);
	i = 0;
	while (src[i] != '\0' && i < nb)
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

	printf("%s \n", ft_strncat(s2, s1, 4));

	char s3[12] = "MAria";
	char s4[10] = "123";

	printf("%s \n", strncat(s4, s3, 4));
}
*/
