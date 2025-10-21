/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 16:27:41 by ridias            #+#    #+#             */
/*   Updated: 2025/10/21 15:40:10 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	int	t;

	t = n - 1;
	if (!dest && !src)
		return (NULL);
	while (t >= 0)
	{
		((char *)dest)[t] = ((char *)src)[t];
		t--;
	}
	((char *)dest)[n] = '\0';
	return (dest);
}
