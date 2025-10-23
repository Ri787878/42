/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 18:30:25 by ridias            #+#    #+#             */
/*   Updated: 2025/10/23 19:21:07 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

size_t	ft_strlen(const char *str);

int	sub_string_check(char *str, char *needle, int needle_size)
{
	while (*str == *needle && needle_size > 0)
	{
		if (*needle == '\0')
			return (1);
		if (*str == '\0')
			return (-1);
		str++;
		needle++;
		needle_size++;
	}
	if (*needle == '\0')
		return (1);
	else
		return (-1);
}

char	*ft_strnstr(const char *str, const char *to_find, size_t len)
{
	size_t	t;
	char	*haystack;
	char	*needle;
	int		needle_size;

	t = 0;
	haystack = (char *)str;
	needle = (char *)to_find;
	needle_size = ft_strlen(needle);
	while (haystack[t] != '\0' && t < len)
	{
		if (sub_string_check(&haystack[t], needle, needle_size) == 1)
			return (&haystack[t]);
		t++;
	}
	return (NULL);
}
