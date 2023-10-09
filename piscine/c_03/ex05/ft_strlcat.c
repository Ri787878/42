/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/09 04:34:35 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/12 13:06:38 by rmano-cl         ###   ########.fr       */
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

unsigned int	ft_strlcat(char *dest, char *src, unsigned int size)
{
	unsigned int	i;
	unsigned int	size1;
	unsigned int	size2;

	size2 = ft_strlen(src);
	size1 = ft_strlen(dest);
	i = 0;
	if (size < 1)
		return (size1);
	while (size1 + i < size1 + size2 && i < size)
	{
		dest[size1 + i] = src[i];
		i++;
	}
	dest[size1 + i] = '\0';
	return (ft_strlen(dest));
}
/*
int main(void) {
    char w1[20] = "12345";
    char w2[10] = "678";
    unsigned int ptr;
    
    ptr = ft_strlcat(w1, w2, 3);
    
    printf("Large string: %s\n\n", w1);
    printf("Small string: %s\n\n", w2);
    
    printf("Command: %u \n", ptr);
}
*/
