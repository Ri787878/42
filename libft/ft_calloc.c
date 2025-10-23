/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 19:28:53 by ridias            #+#    #+#             */
/*   Updated: 2025/10/23 19:56:22 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_bzero(void *s, size_t n);

void	*ft_calloc(size_t number, size_t size)
{
	void	*objects;

	objects = malloc(number * size);
	if (!objects)
		return (NULL);
	ft_bzero(objects, number * size);
	return (objects);
}
