/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <rmano-cl@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/16 13:46:13 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/10/16 14:02:13 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *str1)
{
	int		leng;
	char	*dupped;

	leng = 0;
	while (str1[leng] != '\0')
	{
		leng++;
	}
	if (str1)
	{
		dupped = ft_calloc(leng + 1, 1);
		leng = 0;
		while (str1[leng] != '\0')
		{
			dupped[leng] = str1[leng];
			leng++;
		}
	}
	return (dupped);
}
