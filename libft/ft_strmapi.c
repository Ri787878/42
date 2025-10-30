/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 12:40:34 by ridias            #+#    #+#             */
/*   Updated: 2025/10/29 17:06:51 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlen(const char *str);

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	char	*string;
	int		t;

	t = 0;
	string = malloc(ft_strlen(s));
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
