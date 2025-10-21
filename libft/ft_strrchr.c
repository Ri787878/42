/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 15:59:03 by ridias            #+#    #+#             */
/*   Updated: 2025/10/21 16:06:49 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

size_t	ft_strlen(const char *str);

char	*ft_strrchr(const char *s, int c)
{
	int	n;

	n = (int)ft_strlen(s);
	while (n > 0)
	{
		if (s[n] == c)
			return ((char *)&s[n]);
		n--;
	}
	return (NULL);
}
