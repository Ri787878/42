/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/09 03:42:08 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/09 04:10:09 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int	ft_strncmp(char *s1, char *s2, unsigned int n)
{
	unsigned int	i;

	i = 0;
	while (i < n - 1 && (s1[i] == s2[i] && s1[i] != '\0' && s2[i] != '\0'))
	{
		i++;
	}
	if (n == 0)
		return (0);
	else
		return (s1[i] - s2[i]);
}
/*
int main(void)
{
        char *s1 = "Mara";
        char *s2 = "Maaaiia";

        printf("%d \n", ft_strncmp(s2, s1, 2));

	char *s3 = "Mara";
        char *s4 = "Maaaiia";

        printf("%d \n", strncmp(s4, s3, 2));
}
*/
