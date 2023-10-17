/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <rmano-cl@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/16 13:46:40 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/10/16 13:46:41 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr	(const char *s, int c)
{
	int i;
	char *temp;

	temp = NULL;
	i = 0;
	while(s[i] != '\0')
	{
		if(s[i] == c)
			temp = (char *)s;
		i++;
	}
	return (temp);
}
