/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 12:40:34 by ridias            #+#    #+#             */
/*   Updated: 2025/10/31 13:12:26 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	char			*string;
	unsigned int	t;

	t = 0;
	if (!s || !f)
		return (NULL);
	string = malloc((ft_strlen(s) + 1) * sizeof(char));
	if (!string)
		return (NULL);
	while (s[t])
	{
		string[t] = f(t, s[t]);
		t++;
	}
	string[t] = '\0';
	return (string);
}
