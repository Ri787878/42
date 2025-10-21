/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 14:35:15 by ridias            #+#    #+#             */
/*   Updated: 2025/10/21 15:17:11 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

size_t	ft_strlen(const char *str);

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	int	n;
	int	src_leng;
	int	dst_leng;

	n = 0;
	src_leng = (int)ft_strlen(src);
	dst_leng = (int)ft_strlen(dst);
	if (src == NULL)
		return (0);
	if (dst == NULL || size - dst_leng - 1 < 0)
		return (src_leng);
	while ((n + dst_leng < (int)size - 1) && src[n] != '\0')
	{
		dst[dst_leng + n] = src[n];
		n ++;
	}
	dst[dst_leng + n] = '\0';
	return (dst_leng + src_leng);
}
