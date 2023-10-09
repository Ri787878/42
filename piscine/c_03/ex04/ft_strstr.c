/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/09 04:34:35 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/09 04:34:38 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <stdio.h>
#include <string.h>

char	*ft_strstr(char *str, char *to_find)
{
	int	j;
	int	i;

	i = 0;
	if (*to_find == '\0')
		return (str);
	while (str[i] != '\0')
	{
		j = 0;
		while (str[i + j] != '\0' && str[i + j] == to_find[j])
		{
			if (to_find[j + 1] == '\0')
				return (&str[i]);
			j++;
		}
		i++;
	}
	return (0);
}
/*
int main(void) {
    char *w1 = "abcdefghijklmnop";
    char *w2 = "mn";
    char *ptr;
    
    ptr = strstr(w1, w2);
    
    printf("Large string: %s\n\n", w1);
    printf("Small string: %s\n\n", w2);
    
    printf("Command: %s \n", ptr);
    
    printf("Function: %s\n\n", ft_strstr(w1, w2));
}
*/
