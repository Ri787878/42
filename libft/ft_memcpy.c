/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 16:23:23 by ridias            #+#    #+#             */
/*   Updated: 2025/10/17 16:52:29 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	char	*des;
	char	*sr;
	size_t	t;

	if (!dest && !src)
		return (NULL);
	des = dest;
	sr = (char *)src;
	t = 0;
	while (sr[t] != '\0' && t < n)
	{
		des[t] = sr[t];
		t++;
	}
	return (des);
}
