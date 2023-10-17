/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <rmano-cl@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/16 13:46:35 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/10/16 13:46:36 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *haystack, const char *needle, size_t len) {
	size_t needle_len;
	size_t haystack_len;


	haystack_len = 0;
	needle_len = 0;
	while (needle[needle_len] != '\0')
		needle_len++;
	if (needle_len == 0) {
		return (char *)haystack;
	}
	while (haystack[haystack_len] != '\0' && haystack_len < len) {
		size_t i = 0;
		while (i < needle_len && haystack[haystack_len + i] == needle[i])
			i++;
		if (i == needle_len) {
			return (char *)(haystack + haystack_len);
		}
		haystack_len++;
	}
	return NULL;
}
